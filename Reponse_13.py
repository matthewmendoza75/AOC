import os

def get_data():
    cwd = os.getcwd()
    data = []
    with open(cwd + '/Jour_13_input.txt', 'r') as file:
        lines = file.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("Button A:"):
            # Parse A line
            part = lines[i].split(",")
            Ax_str = part[0].split("X+")[-1].strip()
            Ay_str = part[1].split("Y+")[-1].strip()
            Ax = int(Ax_str)
            Ay = int(Ay_str)

            # Next line: Button B
            i += 1
            part = lines[i].split(",")
            Bx_str = part[0].split("X+")[-1].strip()
            By_str = part[1].split("Y+")[-1].strip()
            Bx = int(Bx_str)
            By = int(By_str)

            # Next line: Prize
            i += 1
            part = lines[i].split(",")
            Px_str = part[0].split("X=")[-1].strip()
            Py_str = part[1].split("Y=")[-1].strip()
            Px = int(Px_str)
            Py = int(Py_str)

            data.append((Ax, Ay, Bx, By, Px, Py))

        i += 1
    return data

def gcd(a, b): # greatest common denominator
    while b != 0:
        a, b = b, a % b
    return a

def solve_machine(Ax, Ay, Bx, By, Px, Py):
    g1 = gcd(Ax, Bx)
    g2 = gcd(Ay, By)
    if Px % g1 != 0 or Py % g2 != 0:
        return None  # No solution possible

    B_max = min(100, Px // Bx) if Bx > 0 else 0
    for B in range(B_max, -1, -1):
        remaining_x = Px - Bx * B
        if Ax != 0 and remaining_x % Ax == 0:
            A = remaining_x // Ax
            if 0 <= A <= 100: # button pressed less then 100 times
                # Check Y equation
                if Ay * A + By * B == Py:
                    # Once we find a solution, it's the one with the most B's possible from this approach.
                    # We can return immediately.
                    cost = 3 * A + 1 * B
                    return cost

    return None

def part1():
    machines = get_data()
    counter = 0
    total_cost = 0
    for (Ax, Ay, Bx, By, Px, Py) in machines:
        cost = solve_machine(Ax, Ay, Bx, By, Px, Py)
        # print("Trying machine: ", counter, " amount ", cost)
        counter += 1
        if cost is not None:
            total_cost += cost

    return total_cost

def solve_machine_optimized(Ax, Ay, Bx, By, Px, Py):
    Px += 10000000000000
    Py += 10000000000000

    denominator = Ax * By - Ay * Bx
    if denominator == 0:  # Division by 0 error later
        return None

    # Solve using the direct computation method
    i = (Px * By - Py * Bx) / denominator
    j = (Px - Ax * i) / Bx if Bx != 0 else 0  # Prevent division by zero again

    # Check if integers and above zero for it to be valid
    if i % 1 == 0 and j % 1 == 0 and \
    i >= 0 and j >= 0:
        cost = int(3 * i + 1 * j)  # Calculate total cost
        return cost

    return None

def part2():
    machines = get_data()
    counter = 0
    total_cost = 0
    for (Ax, Ay, Bx, By, Px, Py) in machines:
        cost = solve_machine_optimized(Ax, Ay, Bx, By, Px, Py)
        # print("Trying machine: ", counter, " amount ", cost)
        counter += 1
        if cost is not None:
            total_cost += cost

    return total_cost
