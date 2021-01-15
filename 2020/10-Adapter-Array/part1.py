def solve(_list):
    one, two, three = 0, 0, 0
    _list += [_list[-1]+3]
    _list = [0] + _list
    for i in range(1, len(_list)):
        if _list[i] - _list[i-1] == 1:
            one += 1
        elif _list[i] - _list[i-1] == 2:
            two += 1
        elif _list[i] - _list[i-1] == 3:
            three += 1
        else:
            break
    return [one, two, three]


if __name__ == "__main__":
    with open('input.txt') as fp:
        lines = fp.readlines()
        lines = list(map(int, lines))
        lines.sort()
    result = solve(lines)
    print(result[0]*result[2])
