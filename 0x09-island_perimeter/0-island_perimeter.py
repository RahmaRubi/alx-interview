#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.
    
    Args:
        grid (list of list of int): 2D grid where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                perimeter += 4  # Add 4 for each land cell
                
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # Check bottom neighbor
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                # Check right neighbor
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    
    return perimeter
