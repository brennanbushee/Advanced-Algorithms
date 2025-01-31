def merge_sort(arr):
    # Base case: if the array is of length 0 or 1, it's already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case: split the array into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in the left half, append them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are remaining elements in the right half, append them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example usage:
arr = [3, -1, 4, 1, 5, 9, -2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)
