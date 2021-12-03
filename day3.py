# day3.py
# Advent of Code - Day 3
# Bevan Lee [engineering@bevanlee.net]

# quick and dirty counter that returns a list
# FIXME there is probably a library that does thisss
def common_bit_counter(input_list):
    c = [0] * len(input_list[0])
    for line in input_list:
        ll = [int(char) for char in line]
        for i in range(len(ll)):
            c[i] += ll[i]
    return c


# Part 1
gamma_lst = []
epsilon_lst = []

# read in file to init variables
with open('input/day3.txt', "r") as f:
    report = [s.strip() for s in f.readlines()]
    binary_length = len(report[0])

# count the number of 1s at each character index
count = common_bit_counter(report)

# add a 1 or 0 depending on majority
for x in count:
    gamma_lst.append(str(int(x > len(report) / 2)))

# epsilon is simply gamma with bits flipped
epsilon_lst = ['0' if x == '1' else '1' for x in gamma_lst]

# flatten lists and cast to int as binary from string
gamma = int(''.join(gamma_lst), 2)
epsilon = int(''.join(epsilon_lst), 2)
print(f"part1={gamma*epsilon}")


# Part 2

# oxygen loop
working_list = report.copy()
# loop over the binary chars, breaking if down to one element
for index in range(binary_length):
    if len(working_list) < 2:
        break
    # recompute the most common bit and extract the index we're up to
    count_at_index = common_bit_counter(working_list)[index]
    most_common_val = '1' if (count_at_index >= len(working_list) / 2) else '0'
    # keep only elements with that char
    working_list = [x for x in working_list if x[index] == most_common_val]

o2_rating = int(working_list[0], 2)

# co2 scrubber loop
working_list = report.copy()
for index in range(binary_length):
    if len(working_list) < 2:
        break
    count_at_index = common_bit_counter(working_list)[index]
    # grab the least common this time
    least_common_val = '1' if (count_at_index < len(working_list) / 2) else '0'
    working_list = [x for x in working_list if x[index] == least_common_val]

co2_scrubber_rating = int(working_list[0], 2)

print(f"part2={o2_rating*co2_scrubber_rating}")
