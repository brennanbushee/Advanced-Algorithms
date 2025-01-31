import heapq


def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, to, from)

    while min_heap:
        cost, to, frm = heapq.heappop(min_heap)
        if to not in visited:
            visited.add(to)
            if frm is not None:
                mst.append((frm, to, cost))

            for neighbor, weight in graph[to].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, to))

    return mst


# Example usage:
graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 3: 1},
    3: {1: 5, 2: 1}
}
print(prim(graph, 0))  # Output: [(0, 1, 1), (1, 2, 2), (2, 3, 1)]
