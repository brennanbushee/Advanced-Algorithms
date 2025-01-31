def can_be_completed(n, a, b):
    def visit(v, adj, stack, visited):
        if visited[v] == -1:  # If currently in the stack (part of the current DFS path), a cycle is found
            return False
        if visited[v] == 1:  # If already fully processed, no need to revisit
            return True

        visited[v] = -1  # Mark as part of the current DFS path
        for u in adj[v]:
            if not visit(u, adj, stack, visited):
                return False

        visited[v] = 1  # Mark as fully processed
        return True

    # Create adjacency list
    adj = {i: [] for i in range(n)}
    for i in range(len(a)):
        adj[a[i]].append(b[i])

    visited = [0] * n  # 0: unvisited, -1: visiting, 1: visited
    for i in range(n):
        if visited[i] == 0:
            if not visit(i, adj, [], visited):
                return False

    return True


def topological_sort(n, edges):
    from collections import defaultdict, deque

    # Initialize the graph and in-degree of each node
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(n)}

    # Build the graph and compute in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Queue for nodes with no incoming edges
    queue = deque([node for node in range(n) if in_degree[node] == 0])

    # List to store the topological order
    topo_order = []

    # Process nodes
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topo_order doesn't contain all nodes, there is a cycle
    if len(topo_order) == n:
        return topo_order
    else:
        return []

# Example usage:
a = [1, 2, 3, 3]
b = [0, 0, 1, 2]
n = 4

# Zip a and b to form the edges list
edges = list(zip(a, b))

# Get the topological order
topo_order = topological_sort(n, edges)
print(topo_order)  # Output will be a valid topological sort or an empty list if a cycle exists



# Example usage:
n = 4

prereqs = [[1, 0],[2, 0],[3, 1],[3, 2]]
a = [5, 4, 3, 2, 1, 0]
b = [2, 0, 4, 1, 3, 5]
print(list(zip(a,b)))


n = 6
print(topological_sort(6, list(zip(a,b))))  # Output: [5, 4, 2, 3, 1, 0] (or any other valid topological order)

# Example usage:
n = 4
a = [0, 1, 2, 3]
b = [1, 2, 3, 1]
print(can_be_completed(n, a, b))  # Output: False
