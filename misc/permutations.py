def permutations(elements):
    n = len(elements)
    visited = [False] * n
    current_permutation = []

    def generate_permutations():
        if len(current_permutation) == n:
            yield tuple(current_permutation)
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                current_permutation.append(elements[i])

                yield from generate_permutations()

                visited[i] = False
                current_permutation.pop()

    yield from generate_permutations()


# Test the permutations generator
def test_permutations():
    # Test case 1: Permutations of a string
    elements1 = "abc"
    expected_permutations1 = [
        ('a', 'b', 'c'), ('a', 'c', 'b'),
        ('b', 'a', 'c'), ('b', 'c', 'a'),
        ('c', 'a', 'b'), ('c', 'b', 'a')
    ]
    assert list(permutations(elements1)) == expected_permutations1

    # Test case 2: Permutations of a list
    elements2 = [1, 2, 3]
    expected_permutations2 = [
        (1, 2, 3), (1, 3, 2),
        (2, 1, 3), (2, 3, 1),
        (3, 1, 2), (3, 2, 1)
    ]
    assert list(permutations(elements2)) == expected_permutations2

    # Test case 3: Permutations of an empty list
    elements3 = []
    expected_permutations3 = [()]
    assert list(permutations(elements3)) == expected_permutations3

    # Test case 4: Permutations of a single element
    elements4 = [4]
    expected_permutations4 = [(4,)]
    assert list(permutations(elements4)) == expected_permutations4



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_permutations()
