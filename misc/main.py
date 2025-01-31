# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def generate_powers_of_5_gen(n):
    i = 0
    while True:
        print(f"{i=}")
        power = 5 ** i
        if power > n:
            break
        yield i
        i += 1


def intersection_gen(A, B):
    B_set = set(B)  # Convert B to a set for O(1) lookups
    return (item for item in A if item in B_set)


# Example usage:


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def two_sum(input: list[int], target: int) -> list[int]:
    i, j = 0, len(input) - 1
    while i < j:
        current = input[i] + input(j)
        if current > target:
            j -= 1
        elif current < target:
            i += 1
        else:
            return [input[i], input[j]]
        return [-1, -1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = [0, 1, 3, 7]
    for item in intersection_gen(A, B):
        print(item)  # Outputs: 1, 3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
