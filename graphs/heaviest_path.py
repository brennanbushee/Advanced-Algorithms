from collections import defaultdict, deque


def find_heaviest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node):
    # Build the graph
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, dag_nodes + 1)}

    for u, v, w in zip(dag_from, dag_to, dag_weight):
        graph[u].append((v, w))
        in_degree[v] += 1

    # Topological Sort (Kahn's Algorithm)
    topo_order = []
    zero_in_degree = deque([node for node in in_degree if in_degree[node] == 0])

    while zero_in_degree:
        node = zero_in_degree.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    # Initialize DP array and path array
    dp = [-float('inf')] * (dag_nodes + 1)
    dp[from_node] = 0
    path = [-1] * (dag_nodes + 1)

    # Traverse nodes in topological order
    for node in topo_order:
        if dp[node] != -float('inf'):  # Only process reachable nodes
            for neighbor, weight in graph[node]:
                if dp[node] + weight > dp[neighbor]:
                    dp[neighbor] = dp[node] + weight
                    path[neighbor] = node

    # Reconstruct the path from to_node to from_node
    if dp[to_node] == -float('inf'):
        return []  # No path exists

    heaviest_path = []
    current_node = to_node
    while current_node != -1:
        heaviest_path.append(current_node)
        current_node = path[current_node]

    return heaviest_path[::-1]


# Example usage
dag_data = {
    "dag_nodes": 4,
    "dag_from": [1, 1, 1, 3],
    "dag_to": [2, 3, 4, 4],
    "dag_weight": [2, 2, 4, 3],
    "from_node": 1,
    "to_node": 4
}

print(find_heaviest_path(dag_data["dag_nodes"], dag_data["dag_from"], dag_data["dag_to"],
                         dag_data["dag_weight"], dag_data["from_node"], dag_data["to_node"]))
