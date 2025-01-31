def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    # Initialize the dp array
    dp = [1] * len(arr)

    # Fill dp array with lengths of LIS ending at each index
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence is the maximum value in dp array
    return max(dp)


# Test Cases
print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 (subsequence: [2, 3, 7, 101])
print(longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))  # Output: 4 (subsequence: [0, 1, 2, 3])
print(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))  # Output: 1 (subsequence: [7])
print(longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # Output: 6 (subsequence: [1, 3, 6, 7, 9, 10])
print(longest_increasing_subsequence([3, 10, 2, 1, 20]))  # Output: 3 (subsequence: [3, 10, 20])
