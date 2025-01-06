import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_06_input.txt', 'r') as file:
        raw_lines = file.readlines()
    data = []
    for line in raw_lines:
        data.append(list(line.strip()))
    return data

def part1():
    grid = get_data()

    #               down     right  up       left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find guard starting position and direction
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in "^>v<":
                guard_position = (row, col)
                current_direction = "^>v<".index(grid[row][col])
                #print(row, " ", col)
                break

    visited_positions = set([guard_position])
    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        # Stop if the guard leaves the grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if the next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4  # Turn right
        else:
            guard_position = next_position  # Move forward
            visited_positions.add(guard_position)

    return len(visited_positions)


def simulate_guard_with_tracking(grid):
    #               down    right    up      left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find guard starting position and direction
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in "^>v<":
                guard_position = (row, col)
                current_direction = "^>v<".index(grid[row][col])
                break

    visited_positions = set([guard_position]) # set because we want unique elements unlike tuple.
    rows, cols = len(grid), len(grid[0])

    while True:
        # Calculate next position
        row, col = guard_position
        dy, dx = directions[current_direction]
        next_position = (row + dy, col + dx)

        # Stop if the guard leaves the grid
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            break

        # Check if the next position is blocked.
        if grid[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4  # Turn right
        else:
            guard_position = next_position  # Move forward
            visited_positions.add(guard_position)

    return visited_positions


def causes_loop_with_obstruction(grid, obstruction_pos, start_pos, start_direction):
    """Simulates the guard"s movement with a new obstruction and checks if it causes a loop."""
    #               down     right  up       left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_now = start_direction
    guard_position = start_pos

    visited_with_direction = set() # unique
    visited_with_direction.add((guard_position, direction_now))

    rows, cols = len(grid), len(grid[0])

    # No need to check if position already obstructed
    if(grid[obstruction_pos[0]][obstruction_pos[1]] == "#"):
        return False

    # Place new obstruction
    grid[obstruction_pos[0]][obstruction_pos[1]] = "#"

    while True:
        y, x = guard_position
        dy, dx = directions[direction_now]
        next_position = (y + dy, x + dx)

        # Check boundry
        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            grid[obstruction_pos[0]][obstruction_pos[1]] = "."  # Remove obstruction for next iteration
            return False # No loop

        # Check if the next position is blocked
        if grid[next_position[0]][next_position[1]] == "#":
            direction_now = (direction_now + 1) % 4  # Turn right
        else:
            guard_position = next_position  # Move forward

        # Check if the guard revisits a position with the same direction
        state = (guard_position, direction_now)
        if state in visited_with_direction:
            grid[obstruction_pos[0]][obstruction_pos[1]] = "."  # Remove obstruction, loop found.
            return True

        visited_with_direction.add(state)


def part2():
    grid = get_data()
    visited_positions = simulate_guard_with_tracking(grid)

    # Find guard"s starting position and direction
    guard_position = None
    guard_direction = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # Debug: Check each cell
            if cell in "^>v<":
                guard_position = (y, x)
                guard_direction = "^>v<".index(cell)  # Map direction to index
                # print(f"Guard found at ({y}, {x}) facing {"^>v<"[guard_direction]}")
                break
        if guard_position:
            break

    loop_positions = []

    # Test only visited positions
    for y, x in visited_positions:
        # Skip the guard"s starting position
        if (y, x) == guard_position:
            continue

        # Check if placing an obstruction at x y causes a loop
        if causes_loop_with_obstruction(grid, (y, x), guard_position, guard_direction):
            loop_positions.append((y, x))

    return len(loop_positions)
