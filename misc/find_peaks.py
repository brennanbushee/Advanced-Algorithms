def count_peaks(arr):
    if not arr:
        return 0

    n = len(arr)
    peak_count = 0

    for i in range(n):
        if (len(arr) == 1):
            return 1
        if (i == n - 1 and arr[i] > arr[i - 1]) or \
            (i == 0 and arr[i] > arr[i + 1]) or \
           (0 < i < n - 1 and arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            peak_count += 1

    return peak_count

# Example usage:
print(count_peaks([3, 2, 4, 5, 1]))  # Output: 2
print(count_peaks([1, 2, 3, 2, 1]))  # Output: 1
print(count_peaks([1, 2, 3, 4, 5]))  # Output: 1
print(count_peaks([5, 4, 3, 2, 1]))  # Output: 1
print(count_peaks([2]))             # Output: 1
print(count_peaks([3,2,1,3,2]))             # Output: 2
print(count_peaks([3,2]))             # Output: 1
print(count_peaks([2, 2, 2, 2, 2]))  # Output: 0
