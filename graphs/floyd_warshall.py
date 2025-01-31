def floyd_warshall(graph):
    dist = {u: {v: float('inf') for v in graph} for u in graph}

    for u in graph:
        dist[u][u] = 0
        for v, weight in graph[u].items():
            dist[u][v] = weight

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example usage:
graph = {
    0: {1: 3, 2: 1},
    1: {2: 7, 3: 5},
    2: {1: 2, 3: 2},
    3: {0: 1}
}
print(floyd_warshall(graph))  # Output: {0: {0: 0, 1: 3, 2: 1, 3: 3}, ...}
