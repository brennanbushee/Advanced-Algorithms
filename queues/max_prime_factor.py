import math


def largest_prime_factor(n):
    # Yield 2 if it's a factor, keep dividing n by 2
    while n % 2 == 0:
        largest = 2
        n //= 2

    # Iterate over odd factors from 3 to sqrt(n)
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % factor == 0:
            largest = factor
            n //= factor

    # If n is a prime number greater than 2
    if n > 2:
        largest = n

    return largest

from math import gcd
import math
from functools import reduce


def max_subarray_sum(input):
    if not input:
        return 0

    max_current = 0
    max_global = 0

    for num in input:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global
def lcm(a, b):
    gcd_value = gcd(a,b)
    ans = abs(a * b) // gcd(a, b)
    print(f"{a=},{b=}, {ans=}, {gcd_value=}=")
    return ans

def smallest_multiple(target):
  return reduce(lcm, range(1, target + 1), 1)

# Example usage:
# print(largest_prime_factor(42))  # Output: 7
# print(largest_prime_factor(25))  # Output: 5
smallest = smallest_multiple(4)
print(smallest)
# Example usage:
arr = [-1, -3, 5, -4, 3, -6, 9, 2]
print(max_subarray_sum(arr))  # Output: 11

arr = [-5, -2, -3, -1]
print(max_subarray_sum(arr))  # Output: 0