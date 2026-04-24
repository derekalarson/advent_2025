filename = "input.txt"


sum = 0


with open(filename, 'r') as file:
    grid = []
    for line in file:
        line = list(line.strip())
        grid.append(line)
    dim = len(grid)

    def in_bounds(row, col):
        if row < 0 or row >= dim: return False
        if col < 0 or col >= dim: return False
        return True

    def check_eight(row, col):
        counter = 0
        if not in_bounds(row-1, col-1) or grid[row-1][col-1] != "@": counter += 1
        if not in_bounds(row-1, col) or grid[row-1][col] != "@": counter += 1
        if not in_bounds(row-1, col+1) or grid[row-1][col+1] != "@": counter += 1
        if not in_bounds(row+1, col-1) or grid[row+1][col-1] != "@": counter += 1
        if not in_bounds(row+1, col+1) or grid[row+1][col+1] != "@": counter += 1
        if not in_bounds(row+1, col) or grid[row+1][col] != "@": counter += 1
        if not in_bounds(row, col+1) or grid[row][col+1] != "@": counter += 1
        if not in_bounds(row, col-1) or grid[row][col-1] != '@': counter += 1
        return counter >= 5


    sum = 0

    for row in range(dim):
        for col in range(dim):
            if grid[row][col] == "@" and check_eight(row, col):
                sum += 1
    
    print(sum)
            

    sum = 0
    
    removed: bool = True
    while(removed):
        removed = False
        for row in range(dim):
            for col in range(dim):
                if grid[row][col] == "@" and check_eight(row, col):
                    sum += 1
                    grid[row][col] = 'x'
                    removed = True

    
    
    print(sum)
