from collections import deque


def is_bipartite(n, edges):
    # Create an adjacency list for the graph
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Array to store colors assigned to all vertices
    color = [-1] * n

    # Function to check if the component containing node is bipartite
    def bfs_check(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with 0

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If the neighbor has not been colored
                    color[neighbor] = 1 - color[node]  # Assign opposite color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # If the neighbor has the same color
                    return False
        return True

    # Check all components of the graph
    for i in range(n):
        if color[i] == -1:  # If the node has not been colored
            if not bfs_check(i):
                return False

    return True


# Example usage:
n = 5
edges = [[0, 1], [1, 2], [0, 4], [1, 3], [4, 3]]
print(is_bipartite(n, edges))  # Output: True
