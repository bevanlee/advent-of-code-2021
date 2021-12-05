# day5.py
# Advent of Code - Day 5
# Bevan Lee [engineering@bevanlee.net]

# this so janky lol
# probably could combine horizontal / vertical plots at least or set x/y step sizes...
def plot_line(m, line):
    # horizontal
    if line[0][1] == line[1][1]:
        y = line[0][1]
        # flip direction if necessary
        if line[0][0] > line[1][0]:
            line = (line[1], line[0])
        # plot the line (inc value)
        for x in range(line[0][0], line[1][0] + 1):
            m[y][x] += 1

    # vertical
    elif line[0][0] == line[1][0]:
        x = line[0][0]
        if line[0][1] > line[1][1]:
            line = (line[1], line[0])
        for y in range(line[0][1], line[1][1] + 1):
            m[y][x] += 1

    # diagonal
    else:
        # swap to make direction left to right
        if line[0][0] > line[1][0]:
            line = (line[1], line[0])
        x = line[0][0]
        # up
        if line[1][1] > line[0][1]:
            for y in range(line[0][1], line[1][1] + 1):
                m[y][x] += 1
                x += 1
        # down
        else:
            for y in range(line[0][1], line[1][1] - 1, -1):
                m[y][x] += 1
                x += 1
    return m


# rewrite
def better_plot_line(m, line):
    # horizontal / vertical
    if line[0][1] == line[1][1] or line[0][0] == line[1][0]:
        # use min/max to do both at once
        for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
            for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                m[y][x] += 1

    # diagonal FIXME
    else:
        # swap to make direction left to right
        if line[0][0] > line[1][0]:
            line = (line[1], line[0])
        x = line[0][0]
        # up
        if line[1][1] > line[0][1]:
            for y in range(line[0][1], line[1][1] + 1):
                m[y][x] += 1
                x += 1
        # down
        else:
            for y in range(line[0][1], line[1][1] - 1, -1):
                m[y][x] += 1
                x += 1
    return m


def print_diagram(m):
    print('---------HYDROTHERMAL-VENTS-MAP-------------')
    for line in m:
        print(''.join(['.' if not x else str(x) for x in line]))
    return m


def main():
    domain = (999, 999)
    lines = []
    with open('input/day5.txt', "r") as f:
        data = [s.strip() for s in f.readlines()]
        for line in data:
            line = [s.split(',') for s in line.split(' -> ')]
            line = [[int(a) for a in pt] for pt in line]
            lines.append(((line[0][0], line[0][1]), (line[1][0], line[1][1])))

    # init map
    m = [[0 for _y in range(domain[0])] for _x in range(domain[1])]

    # plot all lines
    for line in lines:
        better_plot_line(m, line)

    # print_diagram(m)

    # flatten list to sum solution
    flat = [x for y in m for x in y]
    solution = sum(1 for x in flat if x > 1)
    print(f"solution={solution}")


if __name__ == '__main__':
    main()
