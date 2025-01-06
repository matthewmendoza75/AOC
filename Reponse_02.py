import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_02_input.txt', 'r') as file:
        data = file.readlines()
    return data

def is_safe_part1(report):
    levels = report.split()
    int_levels = []
    for level in levels:
        int_levels.append(int(level))
    levels = int_levels

    #Increasing or decreasing
    is_increasing = True
    is_decreasing = True

    for i in range(len(levels) - 1): # Time O(m)
        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False
        if levels[i] >= levels[i + 1]:
            is_increasing = False
        if levels[i] <= levels[i + 1]:
            is_decreasing = False
    return is_decreasing or is_increasing

def part1():
    reports = get_data()
    safe_count = 0
    for report in reports:
        if is_safe_part1(report.strip()):
            safe_count += 1
    return safe_count

def is_safe_part2(report):
    levels = report.split()
    int_levels = []
    for level in levels:
        int_levels.append(int(level))
    levels = int_levels

    def check_safety(levels):
        #Increasing or decreasing
        is_increasing = True
        is_decreasing = True

        for i in range(len(levels) - 1): # Time O(m)
            diff = abs(levels[i+1] - levels[i])

            if diff < 1 or diff > 3:
                return False

            if levels[i] >= levels[i + 1]:
                is_increasing = False
            if levels[i] <= levels[i + 1]:
                is_decreasing = False

        return is_decreasing or is_increasing

    if check_safety(levels):
        return True

    for i in range(len(levels)):
        modified_levels = []
        for j in range(len(levels)):
            if i != j:
                modified_levels.append(levels[j])

        if check_safety(modified_levels):
            return True

def part2():
    reports = get_data()
    safe_count = 0
    for report in reports:
        if is_safe_part2(report.strip()):
            safe_count += 1
    return safe_count
