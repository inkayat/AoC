from collections import defaultdict
import copy

def process(seat_list):
    change = 0
    next_state = copy.deepcopy(seat_list)
    for row in range(len(seat_list)):
        for col in range(len(seat_list[row])):
            occupied = 0
            if seat_list[row][col] == '.':
                continue
            if row-1>=0 and seat_list[row-1][col] == '#':
                occupied += 1
            if row-1>=0 and col-1>=0 and seat_list[row-1][col-1] == '#':
                occupied += 1
            if col-1>=0 and seat_list[row][col-1] == '#':
                occupied += 1
            if row+1<len(seat_list) and col-1>=0 and seat_list[row+1][col-1] == '#':
                occupied += 1
            if row+1<len(seat_list) and seat_list[row+1][col] == '#':
                occupied += 1
            if row+1<len(seat_list) and col+1<len(seat_list[row]) and seat_list[row+1][col+1] == '#':
                occupied += 1
            if col+1<len(seat_list[row]) and seat_list[row][col+1] == '#':
                occupied += 1
            if row-1>=0 and col+1<len(seat_list[row]) and seat_list[row-1][col+1] == '#':
                occupied += 1
            if seat_list[row][col] == 'L' and occupied == 0:
                next_state[row][col] = '#'
                change += 1
            elif seat_list[row][col] == '#' and occupied >= 4:
                change += 1
                next_state[row][col] = 'L'
    if change > 0:
        return next_state
    else:
        return -1


if __name__ == "__main__":
    layout = list()
    memo = defaultdict(lambda:-1)
    with open('input.txt') as fp:
        lines = fp.readlines()
        for line in lines:
            layout.append([i for i in line if i!='\n'])

    while True:
        ret = process(layout)
        if ret == -1:
            break
        else:
            layout = copy.deepcopy(ret)


    result = 0
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            if layout[row][col] == '#':
                result += 1
    print(result)

