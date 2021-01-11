def solve(row, col, f):
    r, c = 0, 0
    for i in range(len(f)):
        if f[i] == 'B':
            row = ((row[0]+row[1])//2+1, row[1])
            r = row[1]
        elif f[i] == 'F':
            row = (row[0],(row[0]+row[1])//2)
            r = row[0]
        elif f[i] == 'R':
            col = ((col[0]+col[1])//2+1, col[1])
            c = col[1]
        elif f[i] == 'L':
            col = (col[0], (col[0]+col[1])//2)
            c = col[0]
    return r*8+c


if __name__ == "__main__":
    with open('input.txt') as fp:
        text = fp.read()
        lines = text.split('\n')
    _max = -1
    for line in lines[0:len(lines)-1]:
        row = (0, 127)
        col = (0, 7)
        ret = solve(row, col, line)
        _max = max(_max, ret)
    print(_max)

