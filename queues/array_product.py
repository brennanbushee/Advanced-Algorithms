def get_product_array(nums):
    mod = 10 ** 9 + 7
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Initialize the result array with 1
    result = [1] * n

    # Step 2: Calculate left cumulative product
    left_product = 1
    for i in range(n):
        result[i] = (result[i] * left_product) % mod
        left_product = nums[i]

    # Step 3: Calculate right cumulative product and update the result array
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] = (result[i] * right_product) % mod
        right_product = (right_product * nums[i]) % mod
    return result


def product_modulo(arr, mod=10**9 + 7):
    result = 1
    for num in arr:
        result = (result * num) % mod
    return result

def apply_function_to_sublists(arr, func):
    return [func(arr[:i] + arr[i+1:]) for i in range(len(arr))]

# Example usage:
arr = [1, 2, 3, 4,5]

# To get the product of each sublist modulo 10**9 + 7
mod = 10**9 + 7
product_mod_results = apply_function_to_sublists(arr, lambda subarr: product_modulo(subarr, mod))
print("Product modulo results:", product_mod_results)

# To get the sum of each sublist modulo 10**9 + 7 (for demonstration, though sum typically won't overflow)
sum_mod_results = apply_function_to_sublists(arr, lambda subarr: sum(subarr) % mod)
print("Sum modulo results:", sum_mod_results)


# Example usage
input_list = [1, 2, 3, 4, 5]
other_list = [4,9,10]
output_list = get_product_array(other_list)
print(output_list)  # Output: [120, 60, 40, 30, 24]
