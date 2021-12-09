# day9.py
# Advent of Code - Day 9
# Bevan Lee [engineering@bevanlee.net]

import math

seen_list = []


def get_low_points(heightmap):
    low_points = []
    for i, row in enumerate(heightmap):
        for j, num in enumerate(row):
            # above
            if i > 0 and num >= heightmap[i-1][j]:
                continue
            # below
            if i < len(heightmap)-1 and num >= heightmap[i+1][j]:
                continue
            # left
            if j > 0 and num >= row[j-1]:
                continue
            # right
            if j < len(row)-1 and num >= row[j+1]:
                continue
            low_points.append((i, j, num))
    return low_points


def find_basin(start_point, heightmap):
    global seen_list
    basin = []
    row, col, val = start_point
    # base case
    if val == 9 or start_point in seen_list:
        return basin
    # add this node
    basin += [start_point]
    seen_list.append(start_point)
    # above
    if row > 0:
        next_node = (row-1, col, heightmap[row-1][col])
        if next_node[2] >= val:
            basin += find_basin(next_node, heightmap)
    # below
    if row < len(heightmap)-1:
        next_node = (row+1, col, heightmap[row+1][col])
        if next_node[2] >= val:
            basin += find_basin(next_node, heightmap)
    # left
    if col > 0:
        next_node = (row, col-1, heightmap[row][col-1])
        if next_node[2] >= val:
            basin += find_basin(next_node, heightmap)
    # right
    if col < len(heightmap[0])-1:
        next_node = (row, col+1, heightmap[row][col+1])
        if next_node[2] >= val:
            basin += find_basin(next_node, heightmap)
    return basin


def main():
    with open('input/day9.txt', "r") as f:
        data = [s.strip() for s in f.readlines()]
        data = [list(s) for s in data]
        heightmap = [[int(s) for s in line] for line in data]

    # Part 1
    low_points = get_low_points(heightmap)
    risk_levels = [pt + 1 for _, _, pt in low_points]
    print("part1=", sum(risk_levels))

    # Part 2
    basins = [find_basin(pt, heightmap) for pt in low_points]
    basins.sort(key=len)
    part2 = math.prod([len(x) for x in basins[-3:]])
    print("part2=", part2)


if __name__ == '__main__':
    main()
