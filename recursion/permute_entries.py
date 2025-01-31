def generate_permutations(arr):
    def permute(start):
        if start == len(arr):
            yield arr[:]
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            print(f"Calling recursively for {arr[start+1:]}, fixing {arr[start]}")
            yield from permute(start + 1)
            arr[start], arr[i] = arr[i], arr[start]  # backtrack

    yield from permute(0)

# Example usage:
arr = [1, 2, 3]
for perm in generate_permutations(arr):
    print(perm)

# For a list of letters
arr_letters = ['a', 'b', 'c']
for perm in generate_permutations(arr_letters):
    print(perm)
