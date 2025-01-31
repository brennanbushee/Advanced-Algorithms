def is_it_a_tree(node_count, edge_start, edge_end):
    # Step 1: Check if the number of edges is exactly n-1
    if len(edge_start) != node_count - 1:
        return False

    # Step 2: Create an adjacency list for the graph
    graph = [[] for _ in range(node_count)]
    for u, v in zip(edge_start, edge_end):
        graph[u].append(v)
        graph[v].append(u)

    # Step 3: Use BFS or DFS to check if the graph is connected
    visited = [False] * node_count

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    # Start DFS from the first node
    visited[0] = True
    dfs(0)

    # If all nodes are visited, the graph is connected
    if not all(visited):
        return False

    return True


# Example usage:
node_count = 4
edge_start = [0, 0, 0]
edge_end = [1, 2, 3]
print(is_it_a_tree(node_count, edge_start, edge_end))  # Output: True
