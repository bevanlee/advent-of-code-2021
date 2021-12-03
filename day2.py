# day2.py
# Advent of Code - Day 2
# Bevan Lee [engineering@bevanlee.net]

# Part 1
subPosition = [0, 0] # [xpos, depth]
with open('input/day2.txt', "r") as f:
    for line in f:
        cmd, value = line.strip().split()
        value = int(value)
        if cmd == 'forward':
            subPosition[0] += value
        elif cmd == 'up':
            subPosition[1] -= value
        elif cmd == 'down':
            subPosition[1] += value

print(subPosition)
print(f"part1={subPosition[0]*subPosition[1]}")

# Part 2
subPosition = [0, 0, 0] # [xpos, depth, aim] aim is positive downward from horizon
with open('input/day2.txt', "r") as f:
    for line in f:
        cmd, value = line.strip().split()
        value = int(value)
        if cmd == 'forward':
            subPosition[0] += value
            subPosition[1] += subPosition[2] * value
        elif cmd == 'up':
            subPosition[2] -= value
        elif cmd == 'down':
            subPosition[2] += value

print(subPosition)
print(f"part2={subPosition[0]*subPosition[1]}")