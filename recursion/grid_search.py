import bisect

def find(query, grid):
    for sublist in grid:
        if sublist[0] <= query <= sublist[-1]:
            # Use binary search to find the query in the sublist
            idx = bisect.bisect_left(sublist, query)
            if idx < len(sublist) and sublist[idx] == query:
                return True
    return False

def search(numbers, queries):
    return [find(q, numbers) for q in queries]

# Example usage
numbers = [
    [1, 2, 3, 12],
    [4, 5, 6, 45],
    [7, 8, 9, 78]
]
queries = [6, 7, 23]
result = search(numbers, queries)
print(result)  # Output: [True, True, False]
