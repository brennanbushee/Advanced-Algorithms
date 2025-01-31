import math
from collections import defaultdict, namedtuple

Edge = namedtuple('Edge', ['u', 'v', 'weight'])


class BinaryLiftingLCA:
    def __init__(self, n):
        self.n = n
        self.l = math.ceil(math.log2(n))
        self.adj = defaultdict(list)
        self.timer = 0
        self.tin = [-1] * n
        self.tout = [-1] * n
        self.up = [[-1] * (self.l + 1) for _ in range(n)]
        self.max_edge = [[0] * (self.l + 1) for _ in range(n)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def dfs(self, v, p, weight):
        self.tin[v] = self.timer
        self.timer += 1
        self.up[v][0] = p
        self.max_edge[v][0] = weight
        for i in range(1, self.l + 1):
            self.up[v][i] = self.up[self.up[v][i - 1]][i - 1]
            self.max_edge[v][i] = max(self.max_edge[v][i - 1], self.max_edge[self.up[v][i - 1]][i - 1])

        for u, w in self.adj[v]:
            if u != p:
                self.dfs(u, v, w)
        self.tout[v] = self.timer
        self.timer += 1

    def is_ancestor(self, u, v):
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def lca_and_max_edge(self, u, v):
        if self.is_ancestor(u, v):
            return u, 0
        if self.is_ancestor(v, u):
            return v, 0

        max_edge = 0
        for i in range(self.l, -1, -1):
            if not self.is_ancestor(self.up[u][i], v):
                max_edge = max(max_edge, self.max_edge[u][i])
                u = self.up[u][i]

        max_edge = max(max_edge, self.max_edge[u][0])
        return self.up[u][0], max_edge

    def preprocess(self, root):
        self.timer = 0
        self.dfs(root, root, 0)


def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    edges.sort(key=lambda edge: edge.weight)
    mst_edges = []
    mst_weight = 0
    for edge in edges:
        if find(edge.u) != find(edge.v):
            union(edge.u, edge.v)
            mst_edges.append(edge)
            mst_weight += edge.weight

    return mst_edges, mst_weight


def find_second_best_mst(n, edges):
    # Step 1: Compute the MST using Kruskal's algorithm
    mst_edges, mst_weight = kruskal(n, edges)
    print(f"{mst_edges=}, {mst_weight=}")
    # Step 2: Create a tree from the MST and preprocess for LCA and max edge
    lca_finder = BinaryLiftingLCA(n)
    for edge in mst_edges:
        lca_finder.add_edge(edge.u, edge.v, edge.weight)

    lca_finder.preprocess(0)

    # Step 3: Find the second-best MST by replacing edges
    second_best_weight = float('inf')
    for edge in edges:
        if edge not in mst_edges:
            u, v, w = edge
            lca, max_edge = lca_finder.lca_and_max_edge(u, v)
            if max_edge > 0:
                possible_weight = mst_weight - max_edge + w
                second_best_weight = min(second_best_weight, possible_weight)

    return second_best_weight if second_best_weight != float('inf') else None


# Example usage
edges = [
    Edge(0, 1, 1), Edge(0, 2, 2), Edge(1, 2, 2),
    Edge(1, 3, 3), Edge(2, 3, 3), Edge(3, 4, 4)
]

#

n = 5
print("Second-best MST weight:", find_second_best_mst(n, edges))
