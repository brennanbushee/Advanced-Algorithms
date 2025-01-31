def intersperse_positives_and_negatives(array):
    positives = [x for x in array if x >= 0]
    negatives = [x for x in array if x < 0]

    result = []
    i, j = 0, 0
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i += 1
        j += 1

    # Append remaining positives or negatives
    if i < len(positives):
        result.extend(positives[i:])
    if j < len(negatives):
        result.extend(negatives[j:])

    return result


# Example usage
arr = [2, 3, -4, -9, -1, -7, 1, -5, -6]
result = intersperse_positives_and_negatives(arr)
print(result)  # Output: [2, -4, 3, -9, 1, -1, -7, -5, -6]
