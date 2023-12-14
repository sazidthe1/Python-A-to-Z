# This is Character Picture Grid Project

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Get the dimensions of the grid
height = len(grid)
width = len(grid[0])

# Loop through each row
for y in range(width):
    # Loop through each column
    for x in range(height):
        # Print the character at the current position, followed by a space
        print(grid[x][y], end='')
    # Print a new line after each row is printed
    print()