def can_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return []  # If total sum is odd, we cannot partition it into two equal parts

    target = total_sum // 2
    n = len(nums)

    # Calculate minimum and maximum possible sum
    min_sum = sum(x for x in nums if x < 0)
    max_sum = sum(x for x in nums if x > 0)

    if target < min_sum or target > max_sum:
        return []  # If target sum is out of the range of possible sums

    # Initialize DP table with offset for negative sums
    offset = -min_sum
    dp = [[False] * (max_sum - min_sum + 1) for _ in range(n + 1)]
    dp[0][offset] = True  # Base case: zero sum (offset by min_sum) is always possible with no elements

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(max_sum - min_sum + 1):
            dp[i][j] = dp[i-1][j]  # Not including the current element
            current_sum = j - offset
            if current_sum >= nums[i-1] and current_sum - nums[i-1] + offset >= 0:
                dp[i][j] = dp[i][j] or dp[i-1][current_sum - nums[i-1] + offset]

    if not dp[n][target + offset]:
        return []  # If target sum is not achievable

    # Backtrack to find the elements that make up the partition
    result = [0] * n
    j = target + offset
    for i in range(n, 0, -1):
        if dp[i][j] and not dp[i-1][j]:
            result[i-1] = 1
            j -= nums[i-1]

    return result

# Example usage
nums = [10, -3, 7, 2, 1, 3]
partition = can_partition(nums)
print(partition)  # Example output: [1, 1, 0, 0, 0, 1]
