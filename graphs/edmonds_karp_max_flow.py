from collections import deque, defaultdict

# Initialize the graph with node count n, capacity, and adjacency list.
n = 0
capacity = []
adj = defaultdict(list)

def bfs(s, t, parent):
    """Performs BFS to find an augmenting path and returns the flow of the found path."""
    # Initialize the parent array to track the path
    for i in range(n):
        parent[i] = -1
    parent[s] = -2

    # Start BFS from the source node
    q = deque([(s, float('inf'))])  # Queue stores pairs of (node, flow)

    while q:
        cur, flow = q.popleft()

        for next_node in adj[cur]:
            # If the next node has not been visited and there is available capacity
            if parent[next_node] == -1 and capacity[cur][next_node] > 0:
                # Update the parent and flow
                parent[next_node] = cur
                new_flow = min(flow, capacity[cur][next_node])

                # If we reach the sink, return the flow
                if next_node == t:
                    return new_flow

                # Otherwise, continue BFS
                q.append((next_node, new_flow))

    # If no augmenting path is found
    return 0

def maxflow(s, t):
    """Calculates the maximum flow from source s to sink t."""
    flow = 0
    parent = [-1] * n

    # Keep finding augmenting paths using BFS
    while True:
        new_flow = bfs(s, t, parent)
        if new_flow == 0:
            break  # No more augmenting paths, so we're done

        # Add the flow of the new augmenting path to the total flow
        flow += new_flow
        cur = t

        # Update the capacities along the path
        while cur != s:
            prev = parent[cur]
            capacity[prev][cur] -= new_flow
            capacity[cur][prev] += new_flow
            cur = prev

    return flow

# Example usage:
n = 6
capacity = [[0] * n for _ in range(n)]

# Fill the adjacency list and capacity matrix based on your graph
# Example: For a graph with 6 nodes and edges with capacities:
adj[0].extend([1, 2])
adj[1].extend([3])
adj[2].extend([4])
adj[3].extend([5])
adj[4].extend([5])

capacity[0][1] = 10
capacity[0][2] = 7
capacity[1][3] = 4
capacity[2][4] = 8
capacity[3][5] = 10
capacity[4][5] = 10

source = 0
sink = 5

# Call maxflow to find the maximum flow from source to sink
max_flow = maxflow(source, sink)
print(f"The maximum flow from node {source} to node {sink} is {max_flow}")
