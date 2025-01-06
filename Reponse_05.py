import os
from collections import defaultdict, deque

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_05_input.txt', 'r') as file:
        data = file.read().strip()

    rules_part, updates_part = data.split("\n\n")
    rules = []
    for line in rules_part.splitlines():
        x, y = line.split("|")
        rules.append((int(x), int(y))) #tuple (X, Y) appended to the list

    # Parse updates into lists of integers
    updates = []
    update_lines = updates_part.splitlines()
    for line in update_lines:
        pages = line.split(",")
        updates.append([int(page) for page in pages])

    return rules, updates

def part1():
    rules, updates = get_data()
    total = 0
    for update in updates:
        # Precompute indices for O(1) lookups
        page_indices = {}
        index = 0
        for page in update:
            page_indices[page] = index
            index += 1

        is_valid = True
        for x, y in rules:
            # Instead of checking membership in a list (O(P)),
            # dictionary allows O(1) membership checks.
            if x in page_indices and y in page_indices: # If both exist in update
                if page_indices[x] > page_indices[y]:  # Rule violated
                    is_valid = False
                    break
        if is_valid:
            middle_page = len(update) // 2 # if even takes from right.
            total += update[middle_page]

    return total

def part2():
    rules, updates = get_data()

    def reorder_update(update, rules):
        # Build a directed graph for pages in the update
        graph = defaultdict(list)  # Tracks which pages must come after others
        in_degree = defaultdict(int)  # Tracks the number of dependencies (incoming edges),
        # if not 0 cant be added to the sorted order because there is another number that must be added first.
        pages_in_update = set(update)  # Only consider rules relevant to this update

        # Add edges based on the rules
        for x, y in rules:
            if x in pages_in_update and y in pages_in_update:
                graph[x].append(y)
                in_degree[y] += 1
                in_degree[x] += 0  # Ensure all nodes appear in in_degree

        # Topological sort to reorder pages
        queue = deque()# Start with nodes having no dependencies (in-degree 0)
        for node in update:
            if in_degree[node] == 0:
                queue.append(node)
        sorted_order = []

        while queue:
            current = queue.popleft()  # Process a node with no dependencies
            sorted_order.append(current)
            for neighbor in graph[current]:  # Reduce dependencies for neighbors
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:  # If a neighbor has no more dependencies, add it to the queue
                    queue.append(neighbor)

        return sorted_order # assuming we always find way to sort it, else make statement to check length but it works.

    incorrect_updates_middle_sum = 0

    for update in updates:
        is_valid = True

        # Check if the update violates any rules
        for x, y in rules:
            if x in update and y in update and update.index(x) > update.index(y):
                is_valid = False
                break

        if not is_valid:
            # Reorder the update and add the middle page to the sum
            reordered_update = reorder_update(update, rules)
            middle_index = len(reordered_update) // 2
            incorrect_updates_middle_sum += reordered_update[middle_index]

    return incorrect_updates_middle_sum
