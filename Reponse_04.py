import os

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_04_input.txt', 'r') as file:
        for line in file:
            data.append(list(line.strip()))
    return data

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    counter = 0
    def checker(x,y,dx,dy):
        for i in range(word_length):
            newX = x + i * dx
            newY = y + i * dy
            #Check if not out of bounds
            if not ((0 <= newX < rows) and (0 <= newY < cols)):
                return False
            #Check if char doesnt match
            if grid[newX][newY] != word[i]:
                return False
        return True

    directions = [
    (0, 1),   # Up
    (1, 0),   # Right
    (1, 1),   # Up Right
    (1, -1),  # Down Right
    (0, -1),  # Down
    (-1, 0),  # Left
    (-1, -1), # Down Left
    (-1, 1)   # Up Left
    ]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if checker(x,y,dx,dy):
                    counter += 1
    return counter

def part1():
    grid = get_data()
    count = count_xmas(grid)
    return count

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    counter = 0

    def is_valid_x_mas(x,y):
        #Out of bounds check
        part1 = False
        part2 = False
        if(((x - 1 >= 0) and (y - 1 >= 0)) and ((x + 1 < rows) and (y + 1 < cols))):
            # Top right to bottom left
            if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
                part1 = True
            if grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M":
                part1 = True

            # Top left to bottom right
            if grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S":
                part2 = True
            if grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M":
                part2 = True

        return part1 and part2

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A":
                if is_valid_x_mas(x,y):
                    counter += 1

    return counter

def part2():
    grid = get_data()
    count = count_x_mas(grid)
    return count
