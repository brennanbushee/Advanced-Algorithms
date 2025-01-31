def find_combinations(arr, target):
    arr.sort()  # Sort the array to handle duplicates easily
    results = []

    def backtrack(start, path, target):
        if target == 0:
            yield path
            return
        if target < 0:
            return
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i - 1]:  # Skip duplicates
                continue
            if arr[i] > target:  # If the number is greater than target, no point in continuing
                break
            yield from backtrack(i + 1, path + [arr[i]], target - arr[i])
    return backtrack(0, [], target)

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

if __name__ == '__main__':
    for combo in combinations_with_replacement('ABC', 2):
        print(combo)


# Example usage:
arr = [12, 13, 11, 15, 9, 8, 16]
target = 24
print(list(find_combinations(arr, target)))  # Output: [[11, 13], [9, 15], [8, 16]]
path = ""
''.join(path)