import os

WIDE = 101
TALL = 103

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_14_input.txt', 'r') as file:
        lines = file.readlines()
    data = []
    for robot in lines: #  format
        sides = robot.split(" ")
        left_side = sides[0]
        right_side = sides[1]
        left_sides = left_side.split(",")
        Px = left_sides[0].split("=")[-1]
        Py = left_sides[1]
        right_sides = right_side.split(",")
        Vx = right_sides[0].split("=")[-1]
        Vy = right_sides[1].strip()
        Px = int(Px)
        Py = int(Py)
        Vx = int(Vx)
        Vy = int(Vy)
        data.append([Px,Py,Vx,Vy])
    return data

def part1():
    robots = get_data()
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for i in range(len(robots)):
        Px,Py,Vx,Vy = robots[i]
        new_Px, new_Py = (Px + Vx * 100),(Py + Vy * 100)
        new_Px, new_Py = (new_Px % WIDE), (new_Py % TALL)

        vertical_middle = WIDE // 2
        horizontal_middle = TALL // 2

        if new_Px < vertical_middle and new_Py < horizontal_middle:
            q1 += 1
        if new_Px > vertical_middle and new_Py < horizontal_middle:
            q2 += 1
        if new_Px < vertical_middle and new_Py > horizontal_middle:
            q3 += 1
        if new_Px > vertical_middle and new_Py > horizontal_middle:
            q4 += 1

    return q1 * q2 * q3 * q4

def part2():
    robots = get_data()
    smallest_answer = 999999999999
    found_at_second = 0
    for second in range(WIDE * TALL): # pattern will repeat every WIDE * TALL times
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        final_grid = [[0]*WIDE for _ in range(TALL)]
        for i in range(len(robots)):
            Px,Py,Vx,Vy = robots[i]
            new_Py, new_Px = (Px + Vx * second),(Py + Vy * second) # swap X and Y coords because its swapped in the examples too
            # for matplotlib
            new_Px, new_Py = (new_Px % TALL), (new_Py % WIDE)
            final_grid[new_Px][new_Py] += 1
            vertical_middle = WIDE // 2
            horizontal_middle = TALL // 2

            if new_Px < vertical_middle and new_Py < horizontal_middle:
                q1 += 1
            if new_Px > vertical_middle and new_Py < horizontal_middle:
                q2 += 1
            if new_Px < vertical_middle and new_Py > horizontal_middle:
                q3 += 1
            if new_Px > vertical_middle and new_Py > horizontal_middle:
                q4 += 1

        answer = q1 * q2 * q3 * q4 # when answer is smallest,
        # robots are bunched together to draw the christmas tree, so one corner will have most robots
        # so when we multiply with other quadrants answer will be smaller
        # If we have 40 robots, answer is smaller if 37 are in Q1 and 1 each in rest = 37
        # If they are evenly split its 10 * 10 * 10 * 10 = 10000
        # So we assume that tree is drawn when smallest answer.
        # Mirrored approach doesnt work

        if (answer < smallest_answer): # find smallest answer
            smallest_answer = answer
            found_at_second = second

    return found_at_second
