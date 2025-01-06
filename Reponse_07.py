import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_07_input.txt', 'r') as file:
        lines = file.readlines()

    equations = []
    for line in lines:
        target, numbers = line.strip().split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations

def evaluate_with_pruning(numbers, target, current_value, index): # recursion
    if index == len(numbers):
        return current_value == target

    # Stop exploring if the current value exceeds the target
    if current_value > target:
        return False # careful if ones exist since adding can result in bigger then multiplying
                     # but it seems theres no cases where it happens.

    if evaluate_with_pruning(numbers, target, current_value + numbers[index], index + 1):
        return True

    if evaluate_with_pruning(numbers, target, current_value * numbers[index], index + 1):
        return True

    return False

def evaluate_equation(target, numbers):
    return evaluate_with_pruning(numbers, target, numbers[0], 1)

def part1():
    equations = get_data()
    total_calibration_result = 0

    for target, numbers in equations:
        if evaluate_equation(target, numbers):
            total_calibration_result += target

    return total_calibration_result


def evaluate_with_pruning(numbers, target, current_value, index): # recursion
    if index == len(numbers):
        return current_value == target

    # # Pruning condition: stop if current value cannot logically lead to target
    if current_value > target:
        return False # careful if ones exist since adding can result in bigger then multiplying
                     # but it seems theres no cases where it happens.

    if evaluate_with_pruning(numbers, target, current_value + numbers[index], index + 1):
        return True

    if evaluate_with_pruning(numbers, target, current_value * numbers[index], index + 1):
        return True

    concatenated_value = int(str(current_value) + str(numbers[index]))
    if evaluate_with_pruning(numbers, target, concatenated_value, index + 1):
        return True

    return False


def part2():
    equations = get_data()
    total_calibration_result = 0

    for target, numbers in equations:
        if evaluate_with_pruning(numbers, target, numbers[0], 1):
            total_calibration_result += target

    return total_calibration_result
