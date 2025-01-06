import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_01_input.txt', 'r') as file:
        data = file.readlines()
        column1 = []
        column2 = []
        for line in data:
            values = line.strip().split()  # Split by whitespace
            if len(values) == 2:  # Ensure there are two values
                column1.append(int(values[0]))  # First column
                column2.append(int(values[1]))  # Second column
    return column1, column2

def part1():
    column1, column2 = get_data()
    a = 0
    while len(column1) and len(column2) > 0:
        # find the abs distance between min values
        a += abs(min(column1) - min(column2))
        # remove minimum values
        column1.remove(min(column1))
        column2.remove(min(column2))
    return a

def part2():
    column1, column2 = get_data()
    b = 0
    for i in column1:
        # count the similarity score in column2
        sim_score = column2.count(i)
        b += i*sim_score
    return b
