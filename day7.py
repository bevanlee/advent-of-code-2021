# day7.py
# Advent of Code - Day 7
# Bevan Lee [engineering@bevanlee.net]

from collections import Counter


def part1(pos, target):
    return abs(pos - target)


def part2(pos, target):
    steps = abs(pos - target)
    return steps * (steps + 1) // 2


def compute_total_fuel(crabs, target):
    fuel = 0
    for key in crabs:
        fuel += part2(key, target) * crabs[key]
    return fuel


def compute_fuels(crabs):
    fuel_costs = {}
    for position in range(max(crabs.keys())):
        fuel_costs[position] = compute_total_fuel(crabs, position)
    return fuel_costs


def main():
    # input_string = '16,1,2,0,4,2,7,1,2,14'
    with open('input/day7.txt', "r") as f:
        input_string = f.readline().strip()
    initial_state = [int(i) for i in input_string.split(',')]
    count = Counter(initial_state)
    fuel_costs = compute_fuels(count)
    min_pos = min(fuel_costs, key=fuel_costs.get)
    print(fuel_costs[min_pos])


if __name__ == '__main__':
    main()
