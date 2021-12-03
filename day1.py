# day1.py
# Advent of Code - Day 1
# Bevan Lee [engineering@bevanlee.net]

with open('input/day1.txt', "r") as f:
    depths = f.read().split("\n")
depths = [int(x) for x in depths]

# SECOND ATTEMPT - BE PYTHONIC
# better sums using list comprehension
part1 = sum(y > x for (x, y) in zip(depths, depths[1:]))
print(f"part1={part1}")
part2 = sum(y > x for (x, y) in zip(depths, depths[3:]))
print(f"part2={part2}")

# First attempt
# lazy c-like iterative solution
prevDepth = 10000000
depthIncreaseCount = 0
for depth in depths:
    if depth - prevDepth > 0:
        depthIncreaseCount += 1
    prevDepth = depth
print(f"part1={depthIncreaseCount}")

# Part 2
# expanding above lazy solution
prevWindow = 100000000
windowIncreaseCount = 0
for x in range(2, len(depths)):
    windowSum = depths[x] + depths[x-1] + depths[x-2]
    if windowSum - prevWindow > 0:
        windowIncreaseCount += 1
    prevWindow = windowSum
print(f"part2={windowIncreaseCount}")
