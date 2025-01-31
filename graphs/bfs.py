from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))

    return dfs_order


# Example usage:
graph = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0, 5, 6},
    3: {1},
    4: {1},
    5: {2},
    6: {2}
}
print(dfs(graph, 0))  # Output: [0, 1, 3, 4, 2, 5, 6]


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            queue.extend(graph[vertex] - visited)

    return bfs_order


# Example usage:
graph = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0, 5, 6},
    3: {1},
    4: {1},
    5: {2},
    6: {2}
}
print(bfs(graph, 0))  # Output: [0, 1, 2, 3, 4, 5, 6]
