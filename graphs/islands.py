def largest_island(grid):
    def dfs(x, y):
        # If out of bounds or at a cell with 0, return 0
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        # Mark the cell as visited by setting it to 0
        grid[x][y] = 0

        # Initialize size of island
        size = 1

        # Visit all 4 adjacent cells (up, down, left, right)
        size += dfs(x + 1, y)
        size += dfs(x - 1, y)
        size += dfs(x, y + 1)
        size += dfs(x, y - 1)

        return size

    max_size = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # If the cell is 1, it is part of an island
                # Get the size of the current island
                current_size = dfs(i, j)
                # Update the maximum size
                max_size = max(max_size, current_size)

    return max_size


def count_islands(matrix):
    def dfs(x, y):
        # If out of bounds or at a cell with 0, return
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == 0:
            return

        # Mark the cell as visited by setting it to 0
        matrix[x][y] = 0

        # Visit all 8 adjacent cells (up, down, left, right, and 4 diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    island_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:  # If the cell is 1, it is part of an island
                island_count += 1  # Increment the island count
                dfs(i, j)  # Perform DFS to mark all cells in this island

    return island_count


# Example usage:
grid = [
    [1, 1, 0],
    [0, 0, 0],
    [1, 0, 1]
]
print(count_islands(grid))  # Output: 2

# Example usage:
grid = [
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 1]
]
print(count_islands(grid))  # Output: 2


empty = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
print(largest_island(empty))  # Output: 5
