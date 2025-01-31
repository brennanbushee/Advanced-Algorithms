
first =   [1, 3, 5]
second=  [2, 4, 6, 0, 0, 0]


def merge_one_into_another(arr1, arr2):
    n = len(arr1)
    arr1.remove()
    # Initialize pointers for arr1, arr2 (non-zero part), and the end of arr2
    i = n - 1
    j = n - 1
    k = 2 * n - 1
    # Merge the arrays from the end to the beginning
    #Invariant: arr[2] from k on always contains the n - k  largest elements.
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr2[k] = arr1[i]
            i -= 1
        else:
            arr2[k] = arr2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in arr1, copy them
    while i >= 0:
        arr2[k] = arr1[i]
        i -= 1
        k -= 1

    # No need to copy remaining elements of arr2 since they are already in place

    return arr2


# Example usage:
#

print(merge_one_into_another(first, second))  # Output: [1, 2, 3, 4, 5, 6]

#merge_one_into_another(first, second)