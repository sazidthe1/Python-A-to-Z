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
width = len(grid)
height = len(grid[0])

# Loop through each row
for y in range(height):
    # Loop through each column
    for x in range(width):
        # Print the character at the current position, followed by a space
        print(grid[x][y], end='')
    # Print a new line after each row is printed
    print()