from functools import reduce


def trailing_zeroes_gen(n):
    power_of_five = 5
    while n >= power_of_five:
        yield n // power_of_five
        power_of_five *= 5


def trailing_zeroes(n):
    return sum(trailing_zeroes_gen(n))


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


if __name__ == '__main__':
    print(factorial(15))
    print(trailing_zeroes(15)) #4
    print(trailing_zeroes(25))  # 6
    print(trailing_zeroes(100)) #24
    print(list(trailing_zeroes_gen(100)))
