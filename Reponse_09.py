import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_09_input.txt', 'r') as file:
        data = file.read().strip()
    return data

def part1():
    disk_map = get_data()
    disk_segments = []

    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))

    # Build disk representation
    blocks = []
    file_id = 0
    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(["."] * length)

    # Compact the disk
    left_walker, right_walker = 0, len(blocks) - 1
    while left_walker < right_walker:
        while left_walker < len(blocks) and blocks[left_walker] != ".":
            left_walker += 1
        while right_walker >= 0 and blocks[right_walker] == ".":
            right_walker -= 1
        if left_walker < right_walker:
            blocks[left_walker], blocks[right_walker] = blocks[right_walker], blocks[left_walker]

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != ".":
            checksum += i * blocks[i]

    return checksum


def part2():
    disk_map = get_data()
    disk_segments = []

    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))

    # Build disk representation
    blocks = []
    file_positions = [] # Metadata for each file: its start position, length, and ID
    file_id = 0
    pos = 0
    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_positions.append((pos, length, file_id))
            pos += length
            file_id += 1
        else:
            blocks.extend([None] * length)
            pos += length

    # Aggregate free spaces into list of tuples
    free_spaces = []
    current_pos = 0
    while current_pos < len(blocks):
        if blocks[current_pos] is None:
            start = current_pos
            while current_pos < len(blocks) and blocks[current_pos] is None:
                current_pos += 1
            free_spaces.append((start, current_pos - start))
        current_pos += 1

    # Move files to the leftmost valid space
    file_count = len(file_positions)
    space_count = len(free_spaces)
    for file_index in range((file_count - 1), -1, -1):  # Iterate through file_positions in reverse order
        start_pos, file_size, file_id = file_positions[file_index]
        for space_index in range(space_count):  # Iterate through free_spaces normally
            space_pos, space_size = free_spaces[space_index]
            if space_pos < start_pos and file_size <= space_size:
                # Move the file
                for j in range(file_size):
                    blocks[start_pos + j] = None
                    blocks[space_pos + j] = file_id
                    # Update free space
                free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
                break

    # Calculate checksum
    checksum = 0
    for i, block in enumerate(blocks):
        if block is not None:
            checksum += i * block

    return checksum
