import os

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_10_input.txt', 'r') as file:
        for line in file:
            data.append(list(map(int, line.strip())))
    return data

def find_trailheads(height_map): # == find zeros
    trailheads = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if height_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(height_map, x, y, current_height, visited):
    rows, cols = len(height_map), len(height_map[0])
    # not out of range, not visited and height is just + 1
    return (0 <= x < rows and 0 <= y < cols and
            (x, y) not in visited and
            height_map[x][y] == current_height + 1)

def dfs(height_map, x, y, visited): # Depth First Search
    stack = [(x, y, 0)]  # (x, y, current height)
    reachable_nines = set()

    while stack:
        cx, cy, current_height = stack.pop()

        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))

        if height_map[cx][cy] == 9:
            reachable_nines.add((cx, cy))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # left, right, down, up
            new_x, new_y = cx + dx, cy + dy
            if is_valid_move(height_map, new_x, new_y, current_height, visited):
                new_height = height_map[new_x][new_y]
                stack.append((new_x, new_y, new_height))

    return len(reachable_nines)

def part1():
    height_map = get_data()
    trailheads = find_trailheads(height_map) # coordinates of zeros
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        total_score += dfs(height_map, trailhead[0], trailhead[1], visited)

    return total_score

def dfs_count_trails(height_map, x, y, visited): # Depth First Search
    rows, cols = len(height_map), len(height_map[0])

    # Base case: Stop if we've reached a height of 9
    if height_map[x][y] == 9:
        return 1

    visited.add((x, y))
    total_trails = 0
    current_height = height_map[x][y]

    # Explore all possible moves recursively
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  #  left, right, down, up
        new_x, new_y = x + dx, y + dy
        # if not out of range, not visited and just +1 in height
        if (0 <= new_x < rows and 0 <= new_y < cols and
                (new_x, new_y) not in visited and
                height_map[new_x][new_y] == current_height + 1):
            total_trails += dfs_count_trails(height_map, new_x, new_y, visited.copy())

    return total_trails

def part2():
    height_map = get_data()
    trailheads = find_trailheads(height_map) # coordinates of zeros
    total_rating = 0

    for trailhead in trailheads:
        visited = set()
        total_rating += dfs_count_trails(height_map, trailhead[0], trailhead[1], visited)

    return total_rating
