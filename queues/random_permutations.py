import random

from collections import Counter
def random_permutation(n):
    arr = list(range(1, n + 1))

    # Fisher-Yates shuffle
    for i in range(n - 1, 0, -1):
        j = int(random.random() * (i + 1))  # Random index from 0 to i
        arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    return arr


# Example usage:
n = 100
randomized_ints = random_permutation(n)
counts = Counter(randomized_ints)
print(len(counts))
print(randomized_ints)
