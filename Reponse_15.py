import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/Jour_15_input.txt', 'r') as file:
        data = file.read().strip()
    s1, s2 = data.split("\n\n")
    return s1, s2

def part1():
    ans = 0
    s1, s2 = get_data()
    g = [list(r) for r in s1.split("\n")]
    n, m = len(g), len(g[0])
    cx, cy = 0 ,0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                cx, cy = i, j
                break

    for move in s2.replace("\n", ""):
        dx, dy = {
            "^": (-1,  0),
            "v": ( 1,  0),
            ">": ( 0,  1),
            "<": ( 0, -1),
        }[move]

    bxs = []
    nx, ny = cx + dx, cy + dy
    while g[nx][ny] == "O":
        bxs.append((nx, ny))
        nx += dx
        ny += dy

    if g[nx][ny] == "#":
        pass
    else:
        assert g[nx][ny] == "."
        target = [(cx, cy)] + bxs + [(nx, ny)]
        for (x1, y1), (x2, y2) in list(zip(target, target[1:]))[::-1]:
            g[x2][y2] = g[x1][y1]
        g[cx][cy] = "."
        cx, cy = cx + dx, cy + dy

    for i in range(n):
        for j in range(m):
            if g[i][j] != "O":
                continue
            ans += 100 * i + j

    return ans


def part2():
    ans = 0
    s1, s2 = get_data()
    g = [list(r) for r in s1.split("\n")]
    g2 = []
    for row in g:
        nrow = []
        for cx in row:
            if cx == "#":
                nrow.append("#")
                nrow.append("#")
            elif cx == "O":
                nrow.append("[")
                nrow.append("]")
            elif cx == ".":
                nrow.append(".")
                nrow.append(".")
            elif cx == "@":
                nrow.append("@")
                nrow.append(".")
            else:
                assert False
        g2.append(nrow)

    g = g2
    n, m = len(g), len(g[0])
    cx, cy = 0 ,0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                cx, cy = i, j
                break

    instruction = s2.replace("\n", "")
    for idx, move in enumerate(instruction):
        dx, dy = {
            "^": (-1,  0),
            "v": ( 1,  0),
            ">": ( 0,  1),
            "<": ( 0, -1),
        }[move]

        c2m = [(cx, cy)]
        i = 0
        impossible = False
        while i < len(c2m):
            x, y = c2m[i]
            nx, ny = x + dx, y + dy
            if g[nx][ny] in "O[]":
                if (nx, ny) not in c2m:
                    c2m.append((nx, ny))

                    if g[nx][ny] == "[":
                        if (nx, ny + 1) not in c2m:
                            c2m.append((nx, ny + 1))

                    if g[nx][ny] == "]":
                        if (nx, ny - 1) not in c2m:
                            c2m.append((nx, ny - 1))

            elif g[nx][ny] == "#":
                impossible = True
                break

            i += 1
        if impossible:
            continue

        new_grid = [[g[i][j] for j in range(m)] for i in range(n)]

        for x, y in c2m:
            new_grid[x][y] = "."
        for x, y in c2m:
            new_grid[x + dx][y + dy] = g[x][y]

        g = new_grid
        cx += dx
        cy += dy

    for i in range(n):
        for j in range(m):
            if g[i][j] != "[":
                continue
            ans += 100 * i + j

    return ans
