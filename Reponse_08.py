import os
from collections import defaultdict, deque

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_08_input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def part1():
    lines = get_data()
    antennas = []
    valid_antenna_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in valid_antenna_chars:
                antennas.append((x, y, char))

    # Group antennas by frequency
    frequency_map = defaultdict(list)
    for x, y, freq in antennas:
        frequency_map[freq].append((x, y))

    unique_antinodes = set() # set has unique elements only
    for freq, positions in frequency_map.items():
        # Skip frequencies with only one antenna
        if len(positions) < 2:
            continue

        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                step_x = x2 - x1
                step_y = y2 - y1
                antinode1 = (x1 - step_x, y1 - step_y)
                antinode2 = (x2 + step_x, y2 + step_y)
                # Add to unique locations if valid
                if 0 <= antinode1[0] < len(lines[0]) and 0 <= antinode1[1] < len(lines):
                    unique_antinodes.add(antinode1)
                if 0 <= antinode2[0] < len(lines[0]) and 0 <= antinode2[1] < len(lines):
                    unique_antinodes.add(antinode2)

    return len(unique_antinodes)

def part2():
    lines = get_data()
    antennas = []
    valid_antenna_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in valid_antenna_chars:
                antennas.append((x, y, char))

    # Group antennas by frequency
    frequency_map = defaultdict(list)
    for x, y, freq in antennas:
        frequency_map[freq].append((x, y))

    unique_antinodes = set() # set has unique elements only
    for freq, positions in frequency_map.items():
        # Skip frequencies with only one antenna
        if len(positions) < 2:
            continue

        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                step_x = x2 - x1
                step_y = y2 - y1
                # Step along the line in both directions and add antinodes
                for direction in [-1, 1]:
                    k = 1  # Start stepping
                    while True:
                        new_x = x1 + direction * k * step_x
                        new_y = y1 + direction * k * step_y
                        if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
                            unique_antinodes.add((new_x, new_y))
                            k += 1
                        else:
                            break  # Out of bounds

    # Add all antenna positions to unique antinodes if they belong to a frequency with more than one antenna
    for freq, positions in frequency_map.items():
        if len(positions) > 1:
            for x, y in positions:
                unique_antinodes.add((x, y))

    return len(unique_antinodes)
