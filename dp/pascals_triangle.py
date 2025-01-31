


def generate_pascals_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each triangle[i][j] is the sum of triangle[i-1][j-1] and triangle[i-1][j]
            row.append((triangle[i - 1][j - 1] + triangle[i - 1][j]) % MOD)
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


# Example usage:
n = 6
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)
