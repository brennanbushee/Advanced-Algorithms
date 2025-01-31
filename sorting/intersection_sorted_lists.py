def find_intersection(arr1, arr2, arr3):
    # Initialize pointers for all three lists
    i, j, k = 0, 0, 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If all three elements are equal, add it to the result and move all pointers forward
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Otherwise, move the pointer of the smallest element forward
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    # If result is empty, return [-1]
    return result if result else [-1]

def max_three(input):
    # Sort the list in ascending order
    input.sort()

    # The maximum product can be either:
    # 1. The product of the three largest numbers (last three numbers after sorting)
    # 2. The product of the two smallest numbers (first two numbers after sorting) and the largest number (last number after sorting)
    max_product = max(input[-1] * input[-2] * input[-3],
                      input[0] * input[1] * input[-1])

    return max_product

if __name__ == '__main__':
    arr1 = [2, 5, 10],
    arr2 = [2, 3, 4, 10],
    arr3 = [2, 4, 10]

    # Output:[2, 10]
    # Example Two

    arr1 = [1, 2, 3],
    arr2 = [],
    arr3 = [2, 2]

    # Output:[-1]
    # Example Three

    arr1 = [1, 2, 2, 2, 9],
    arr2 = [1, 1, 2, 2],
    arr3 = [1, 1, 1, 2, 2, 2]
    # Output: [1, 2, 2]