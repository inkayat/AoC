from collections import defaultdict
import copy

def search(container, row, col, direction):
    is_find = False
    if direction == 'up':
        while row>=1:
            if container[row-1][col] == '#':
                is_find = True
                break
            elif container[row-1][col] == 'L':
                break
            row -= 1
    elif direction == 'up-left':
        while row>=1 and col>=1:
            if container[row-1][col-1] == '#':
                is_find = True
                break
            elif container[row-1][col-1] == 'L':
                break
            row -= 1
            col -= 1
    elif direction == 'left':
        while col>=1:
            if container[row][col-1] == '#':
                is_find = True
                break
            elif container[row][col-1] == 'L':
                break
            col -= 1
    elif direction == 'left-down':
        while row+1<len(container) and col>=1:
            if container[row+1][col-1] == '#':
                is_find = True
                break
            elif container[row+1][col-1] == 'L':
                break
            row += 1
            col -= 1
    elif direction == 'down':
        while row+1<len(container):
            if container[row+1][col] == '#':
                is_find = True
                break
            elif container[row+1][col] == 'L':
                break
            row += 1
    elif direction ==  'down-right':
        while row+1<len(container) and col+1<len(container[0]):
            if container[row+1][col+1] == '#':
                is_find = True
                break
            elif container[row+1][col+1] == 'L':
                break
            col += 1
            row += 1
    elif direction == 'right':
        while col+1<len(container[0]):
            if container[row][col+1] == '#':
                is_find = True
                break
            elif container[row][col+1] == 'L':
                break
            col += 1
    elif direction == 'right-up':
        while col+1<len(container[0]) and row>=1:
            if container[row-1][col+1] == '#':
                is_find = True
                break
            elif container[row-1][col+1] == 'L':
                break
            col += 1
            row -= 1
    return is_find


def process(seat_list):
    change = 0
    next_state = copy.deepcopy(seat_list)
    for row in range(len(seat_list)):
        for col in range(len(seat_list[row])):
            occupied = 0
            if seat_list[row][col] == '.':
                continue
            if search(seat_list, row, col, 'up'):
                occupied += 1
            if search(seat_list, row, col, 'up-left'):
                occupied += 1
            if search(seat_list, row, col, 'left'):
                occupied += 1
            if search(seat_list, row, col, 'left-down'):
                occupied += 1
            if search(seat_list, row, col, 'down'):
                occupied += 1
            if search(seat_list, row, col, 'down-right'):
                occupied += 1
            if search(seat_list, row, col, 'right'):
                occupied += 1
            if search(seat_list, row, col, 'right-up'):
                occupied += 1
            if seat_list[row][col] == 'L' and occupied == 0:
                next_state[row][col] = '#'
                change += 1
            elif seat_list[row][col] == '#' and occupied >= 5:
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


