# day6.py
# Advent of Code - Day 6
# Bevan Lee [engineering@bevanlee.net]

from collections import Counter


# Part 1
def model_day(state):
    downtick = [i-1 for i in state]
    newstate = []
    for age in downtick:
        if age < 0:
            newstate.append(6)
            newstate.append(8)
        else:
            newstate.append(age)
    return newstate


# Part 2
def better_model_day(state):
    num_new_fish = state.pop(0)
    state[6] += num_new_fish
    state.append(num_new_fish)
    return state

def main():
    #input_string = '3,4,3,1,2'
    with open('input/day6.txt', "r") as f:
        input_string = f.readline().strip()
    initial_state = [int(i) for i in input_string.split(',')]
    count = Counter(initial_state)
    # state = initial_state
    state = [count[x] for x in range(9)]
    for i in range(256):
        state = better_model_day(state)

    print(sum(state))


if __name__ == '__main__':
    main()
