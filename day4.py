# day4.py
# Advent of Code - Day 4
# Bevan Lee [engineering@bevanlee.net]

# Functions

def stamp_number(b, num):
    for index in range(len(b)):
        b[index] = [(num, True) if x[0] == num else x for x in b[index]]
    return b


def check_winner(b):
    # horizontal
    for line in b:
        if all(stamped is True for (_, stamped) in line):
            return True
    # vertical
    # rotate list and check again
    rotated_b = list(zip(*b[::-1]))
    for line in rotated_b:
        if all(stamped is True for (_, stamped) in line):
            return True
    # otherwise not a winner
    return False


def calculate_score(b, num):
    unmarked = [int(x[0]) for line in b for x in line if x[1] is False]
    return sum(unmarked) * num


def print_board(b):
    for line in b:
        nums = [' '+x[0] if len(x[0]) < 2 else x[0] for x in line]
        print(' '.join(nums))


# Part 1
with open('input/day4.txt', "r") as f:
    draw_queue = f.readline().strip().split(',')
    base_boards = [s.strip().split('\n') for s in f.read().split('\n\n')]
    base_boards = [[line.split() for line in board] for board in base_boards]

# add a 'stamped' flag
boards = [[[(x, False) for x in line] for line in board] for board in base_boards]

# numbers call loop
while draw_queue:
    number_call = draw_queue.pop(0)
    for board in boards:
        # mark board
        stamp_number(board, number_call)
        # check for win
        if check_winner(board):
            print(f"Winning board score = {calculate_score(board, int(number_call))}")
            print_board(board)
            # exit()
            # Part 2
            # remove board from list and continue
            boards.remove(board)
