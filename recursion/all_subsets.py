def generate_subsets(arr):
    def subsets(index, path):
        print(f"Valid subset:{path=}")
        yield path
        for i in range(index, len(arr)):
            print(f"Calling recursively for remaining elements {arr[i + 1:]}, including {arr[i]}")
            yield from subsets(i + 1, path + [arr[i]])

    yield from subsets(0, [])

# Example usage:
arr = [1, 2, 3]
for subset in generate_subsets(arr):
    print(subset)

# For a set of letters
arr_letters = ['a', 'b', 'c', 'd']
for subset in generate_subsets('abcd'):
    print(subset)
