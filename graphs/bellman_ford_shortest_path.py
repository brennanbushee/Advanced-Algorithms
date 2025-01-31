def bellman_ford(graph, start):
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distance


# Example usage:
graph = {
    0: {1: 1, 2: 4},
    1: {2: 2, 3: 5},
    2: {3: 1},
    3: {}
}
print(bellman_ford(graph, 0))  # Output: {0: 0, 1: 1, 2: 3, 3: 4}
