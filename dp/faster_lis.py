import bisect

import bisect

def lis(arr):
    n = len(arr)
    INF = float('inf')
    working_copy = [INF] * (n + 1)
    working_copy[0] = -INF
    prev = [-1] * n  # Array to track the predecessors of elements in the subsequence
    sub_pos = [-1] * (n + 1)  # Array to track the positions of elements in the subsequence

    for i in range(n):
        # Return the index where item x would go in list a, assuming a is sorted.
        l = bisect.bisect_right(working_copy, arr[i])
        if working_copy[l - 1] < arr[i] < working_copy[l]:
            working_copy[l] = arr[i]
            sub_pos[l] = i
            prev[i] = sub_pos[l - 1]

    # Find the length of the LIS
    length = sum(1 for i in range(1, n+1) if working_copy[i] < INF)
    # for l in range(n + 1):
    #     if working_copy[l] < INF:
    #         length = l

    # Reconstruct the LIS using the 'prev' array
    lis_sequence = []
    p = sub_pos[length]
    while p != -1:
        lis_sequence.append(arr[p])
        p = prev[p]

    lis_sequence.reverse()  # The sequence was built backwards, so reverse it

    return lis_sequence

# Example usage:
a = [3, 10, 2, 1, 20]
print(lis(a))  # Output: [3, 10, 20]


# Example usage:
a = [3, 10, 2, 1, 20]
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 (subsequence: [2, 3, 7, 101])
print(lis([0, 1, 0, 3, 2, 3]))  # Output: 4 (subsequence: [0, 1, 2, 3])
print(lis([7, 7, 7, 7, 7, 7, 7]))  # Output: 1 (subsequence: [7])
print(lis([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # Output: 6 (subsequence: [1, 3, 6, 7, 9, 10])
print(lis([3, 10, 2, 1, 20]))  # Output: 3 (subsequence: [3, 10, 20])
print(lis(a))  # Output: 3
