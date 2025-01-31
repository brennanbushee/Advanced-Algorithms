class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def BFS(node, adj):
    from collections import deque

    q = deque([node])
    visited = set()

    while q:
        v = q.popleft()  # Pop from the left for FIFO (queue)
        if v.value not in visited:
            visited.add(v.value)
            for u in v.neighbors:
                if u.value not in adj:
                    adj[u.value] = [v.value]
                else:
                    adj[u.value].append(v.value)
                if u.value not in visited:
                    q.append(u)

    return adj


def create_transpose(node):
    if node is None:
        return None

    adj = {}
    BFS(node, adj)

    new_nodes = {}

    for k in adj.keys():
        new_nodes[k] = GraphNode(k)

    for u, neighbors in adj.items():
        for v in neighbors:
            new_nodes[u].neighbors.append(new_nodes[v])

    # Return any node from the new graph
    return new_nodes[next(iter(new_nodes))]


# Example usage:
# Creating the original graph
node0 = GraphNode(0)
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)

node0.neighbors = [node1, node2]
node1.neighbors = [node2]
node2.neighbors = [node0, node3]
node3.neighbors = [node1]

# Creating the transpose graph
transpose_node = create_transpose(node0)


# Printing the transpose graph's adjacency list
def print_graph(node):
    visited = set()

    def dfs(v):
        if v.value in visited:
            return
        visited.add(v.value)
        print(f"Node {v.value}: {[n.value for n in v.neighbors]}")
        for neighbor in v.neighbors:
            dfs(neighbor)

    dfs(node)


print_graph(transpose_node)
