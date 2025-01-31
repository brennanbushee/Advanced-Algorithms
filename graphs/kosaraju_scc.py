from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)  # Original graph

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.dfs(u, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed_graph = Graph(self.vertices)
        for v in self.graph:
            for u in self.graph[v]:
                transposed_graph.add_edge(u, v)
        return transposed_graph

    def fill_order(self, visited, stack):
        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

    def dfs_on_transposed(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for u in self.graph[v]:
            if not visited[u]:
                self.dfs_on_transposed(u, visited)

    def find_sccs(self):
        stack = []
        visited = [False] * self.vertices

        # Step 1: Run DFS on the original graph and fill the stack
        self.fill_order(visited, stack)

        # Step 2: Transpose the graph
        transposed_graph = self.transpose()

        # Step 3: Run DFS on the transposed graph using the vertex in order of their finishing time
        visited = [False] * self.vertices
        while stack:
            v = stack.pop()
            if not visited[v]:
                transposed_graph.dfs_on_transposed(v, visited)
                print()  # Newline after each SCC

# Example Usage:
g = Graph(6)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 0)
g.add_edge(2, 1)
g.add_edge(3, 4)
g.add_edge(3, 5)

print("Strongly Connected Components are:")
g.find_sccs()
