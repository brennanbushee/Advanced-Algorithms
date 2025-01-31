def find_zero_sum_subarray(arr):
    cum_sum = 0
    cum_sum_map = {0: -1}  # Initialize with 0 sum at index -1 to handle the case when subarray starts from index 0

    for index, value in enumerate(arr):
        cum_sum += value

        if cum_sum in cum_sum_map:
            return [cum_sum_map[cum_sum] + 1, index]

        cum_sum_map[cum_sum] = index

    return [-1]


# Example usage:
arr1 = [5, 1, 2, -3, 7, -4]
arr2 = [1, 2, 3, 5, -9]

print(find_zero_sum_subarray(arr1))  # Output could be [1, 3] or [3, 5]
print(find_zero_sum_subarray(arr2))  # Output should be [-1]
