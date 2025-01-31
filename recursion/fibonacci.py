from functools import lru_cache


def fibonacci_recursive_slow(n):
    if n <= 1:
        return n
    return fibonacci_recursive_slow(n - 1) + fibonacci_recursive_slow(n - 2)


@lru_cache(maxsize=3)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

#Old-fashioned memoization
def fibonacci_memo_uncached(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo_uncached(n - 1, memo) + fibonacci_memo_uncached(n - 2, memo)
    return memo[n]

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 30
for fib in (fibonacci_memo(i) for i in range(n)):
    print(fib)
print("Now for the slow way: ")
print(fibonacci_recursive_slow(n))




