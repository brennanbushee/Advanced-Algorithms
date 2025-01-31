import random


# Efficiently find the kth-smallest element in a list.
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    # Randomly select a pivot
    pivot = random.choice(arr)

    # Partition the array into elements less than and greater than the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Determine the position of the pivot
    L, E, G = len(less), len(equal), len(greater)

    if k < L:
        return quickselect(less, k)
    elif k < L + E:
        return equal[0]
    else:
        return quickselect(greater, k - L - E)


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
k = 3  # Find the 4th smallest element (1-based index)
print(quickselect(arr, k))  # Output: 3
