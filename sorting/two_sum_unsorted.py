def find_two_sum_indices(numbers, target):
    num_to_index = {}

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return [-1, -1]

from random import  shuffle
# Example usage:
numbers = [2, 7, 11, 15]
shuffle(numbers)
print(f"Scrambled list: {numbers=}")
target = 9
print(find_two_sum_indices(numbers, target))  # Output: [0, 1]

# Example with no solution:
target = 20
print(find_two_sum_indices(numbers, target))  # Output: [-1, -1]

# Example with negative numbers:
numbers = [-1, -2, -3, -4, -5]
shuffle(numbers)
print(f"Scrambled list: {numbers=}")
target = -8
print(find_two_sum_indices(numbers, target))  # Output: [2, 4]
