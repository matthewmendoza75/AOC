import re
import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_03_input.txt', 'r') as file:
        data = file.read()
    return data

def part1():
    corrupted_memory = get_data()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)" #Grouping
    matches = re.findall(pattern, corrupted_memory)
    result_sum = 0
    for x,y in matches:
        result_sum += int(x) * int(y)
    return result_sum

def part2():
    corrupted_memory = get_data()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)" #Grouping
    control_pattern = r"(do\(\)|don't\(\))"
    all_matches = re.findall(f"{control_pattern}|{pattern}", corrupted_memory)
    result_sum = 0
    mul_enabled = True

    for string_match in all_matches:
        if string_match[0]:
            if string_match[0] == "do()":
                mul_enabled = True
            elif string_match[0] == "don't()":
                mul_enabled = False
        elif string_match[1] and string_match[2]:
            if mul_enabled:
                x, y = int(string_match[1]), int(string_match[2])
                result_sum += x * y

    return result_sum
