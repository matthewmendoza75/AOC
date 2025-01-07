import os
from functools import cache

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_11_input.txt', 'r') as file:
        line = file.readline().strip()
    for number in line.split():
        data.append(int(number))
    return data

def part1():
    stones = get_data()
    blinks = 25
    for i in range(blinks):
        # print(i) # to see how fast it goes
        new_stones = []
        for stone in stones:
            if stone == 0: # if stone is 0
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0: # if even digits
                half_len = len(str(stone)) // 2
                left_half = int(str(stone)[:half_len])
                right_half = int(str(stone)[half_len:])
                new_stones.extend([left_half, right_half])
            else: # otherwise, multiply stone by 2024
                new_stones.append(stone * 2024) # order doesnt matter so just append them
        stones = new_stones

    return len(stones)

@cache
def process_stone(value, remaining_blinks):
    if remaining_blinks == 0:  # Base case: no blinks left
        return 1
    if value == 0:  # if stone is 0
        return process_stone(1, remaining_blinks - 1)

    value_str = str(value)
    length = len(value_str)

    if length % 2 == 0:  # if even digits
        midpoint = length // 2
        left_half = int(value_str[:midpoint])
        right_half = int(value_str[midpoint:])
        return process_stone(left_half, remaining_blinks - 1) + process_stone(right_half, remaining_blinks - 1)
    else:  # otherwise, multiply stone by 2024
        new_value = value * 2024
        return process_stone(new_value, remaining_blinks - 1)

def part2():
    stones = get_data()
    total_stones = 0
    for stone in stones: # for each stone we see how many they make
        total_stones += process_stone(stone, 75)
    return total_stones
