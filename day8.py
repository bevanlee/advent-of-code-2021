# day8.py
# Advent of Code - Day 8
# Bevan Lee [engineering@bevanlee.net]

from collections import Counter


# oops dictionary is wrong way around... ah well too late to fix...
def find_digit_by_pattern(pattern_dict, p):
    return next(num for num, seg_string in pattern_dict.items() if seg_string == p)


def find_digit_by_len(patterns_lst, length):
    tmp = [x for x in patterns_lst if len(x) == length]
    return tmp[0]


def decode_pattern(patterns_lst):
    # easy unique digits
    patterns_dict = {1: find_digit_by_len(patterns_lst, 2), 4: find_digit_by_len(patterns_lst, 4),
                     7: find_digit_by_len(patterns_lst, 3), 8: find_digit_by_len(patterns_lst, 7)}
    for x in [1, 4, 7, 8]:
        patterns_lst.remove(patterns_dict[x])

    # numbers with one missing seg
    tmp = [x for x in patterns_lst if len(x) == 6]  # 0, 6, 9
    # number 6
    for num in tmp:
        missing_seg = patterns_dict[8] - num  # get single seg
        if missing_seg <= patterns_dict[1]:
            patterns_dict[6] = num
            patterns_lst.remove(num)

    # numbers 9 and 0
    tmp = [x for x in patterns_lst if len(x) == 6]  # 0, 6
    for num in tmp:
        missing_seg = patterns_dict[8] - num  # get single seg
        if missing_seg <= patterns_dict[4]:
            patterns_dict[0] = num
            patterns_lst.remove(num)
        else:
            patterns_dict[9] = num
            patterns_lst.remove(num)

    # find number 2
    for num in patterns_lst:
        tmp = num - patterns_dict[4]
        if not tmp <= patterns_dict[9]:
            patterns_dict[2] = num
            patterns_lst.remove(num)

    # last two numbers
    num = patterns_lst.pop()
    if patterns_dict[7] <= num:  # 3, 5
        patterns_dict[3] = num
        patterns_dict[5] = patterns_lst.pop()
    else:  # 5, 3
        patterns_dict[5] = num
        patterns_dict[3] = patterns_lst.pop()
    # well that was messy ha
    return patterns_dict


def part1(data):
    digits = []
    for line in data:
        unique_patterns, output_vals = line.split('|')
        output_vals = output_vals.split()
        for x in output_vals:
            digits.append(x)
    c = Counter(digits)
    special_digits = [x for x in c.keys() if len(x) in [2, 4, 3, 7]]
    print(sum(c[k] for k in special_digits))
    return


def part2(data):
    lines = []
    for line in data:
        pattern_vals, output_vals = line.split('|')
        pattern_vals = pattern_vals.split()
        output_vals = output_vals.split()
        patterns = [set(item) for item in pattern_vals]
        outputs = [set(item) for item in output_vals]
        pattern_dict = decode_pattern(patterns)
        output = int(''.join([str(find_digit_by_pattern(pattern_dict, x)) for x in outputs]))

        lines.append(output)

    print(sum(lines))
    return


def main():
    with open('input/day8.txt', "r") as f:
        data = [s.strip() for s in f.readlines()]
    part1(data)
    # data = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    part2(data)


if __name__ == '__main__':
    main()
