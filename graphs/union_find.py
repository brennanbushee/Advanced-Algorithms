class DynamicConnectivity:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n  # Initially, each node is its own component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

            self.components -= 1  # Merging two components reduces the count

    def add_edge(self, u, v):
        self.union(u, v)

    def count_connected_components(self):
        return self.components


# Example usage:
n = 6  # Number of nodes
edges = [(0, 1), (1, 2), (0,3), (3, 4), (0,4)]

dc = DynamicConnectivity(n)

# Add initial edges
for u, v in edges:
    dc.add_edge(u, v)

print(f"Initial connected components: {dc.count_connected_components()}")  # Should return 2
# Dynamically add a new edge that does not change the component count
dc.add_edge(0, 2)
print(f"Connected components after adding edge (0, 2): {dc.count_connected_components()}")  # Should still return 1

# Dynamically add a new edge and recount
dc.add_edge(2, 5)
print(f"Connected components after adding edge (2, 3): {dc.count_connected_components()}")  # Should return 1

