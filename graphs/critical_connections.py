def find_critical_connections(number_of_servers, connections):
    # Initialize graph adjacency list
    graph = [[] for _ in range(number_of_servers)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize variables for DFS
    discovery_time = [-1] * number_of_servers
    low = [0] * number_of_servers
    visited = [False] * number_of_servers
    parent = [-1] * number_of_servers
    time = 0
    critical_connections = []

    def dfs(u):
        nonlocal time
        visited[u] = True
        discovery_time[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if low[v] > discovery_time[u]:
                    critical_connections.append([u, v])

            elif v != parent[u]:
                low[u] = min(low[u], discovery_time[v])

    # Start DFS from all nodes to ensure all components are covered
    for i in range(number_of_servers):
        if not visited[i]:
            dfs(i)

    return critical_connections

# Example usage
n = 6
edges = [
    [1, 2],
    [2, 5],
    [1, 5],
    [5, 3],
    [4, 3],
    [5, 4],
    [0, 5]
]
print("Critical Connections (Bridges) in the graph are:")
print(find_critical_connections(n, edges))  # Should return [[0, 5]]
