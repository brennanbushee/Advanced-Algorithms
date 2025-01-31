def find_two_numbers_that_sum_to_target(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [numbers[left], numbers[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


# Example usage:
numbers = [-10, -3, 1, 2, 4, 6, 8, 10]
target = 7
print(find_two_numbers_that_sum_to_target(numbers, target))  # Output: [-3, 10]

# Example with no solution:
target = 20
print(find_two_numbers_that_sum_to_target(numbers, target))  # Output: [-1, -1]

# Example with negative target:
target = -9
print(find_two_numbers_that_sum_to_target(numbers, target))  # Output: [-10, 1]
