#!/usr/bin/python3
“””
 Function that computes the perimeter of an island
“””
def island_perimeter(grid):
    def is_valid_cell(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check only land cells
            if grid[i][j] == 1:
                # Check adjacent cells (up, down, left, right)
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

                # Check each neighbor
                for ni, nj in neighbors:
                    if not is_valid_cell(ni, nj) or grid[ni][nj] == 0:
                        # If the neighbor is out of bounds or is water, increase the perimeter
                        perimeter += 1

                # Check if the current cell is at the border of the grid
                if i == 0 or i == len(grid) - 1:
                    perimeter += 1
                if j == 0 or j == len(grid[0]) - 1:
                    perimeter += 1

    return perimeter
result = island_perimeter(grid)
print(result)

