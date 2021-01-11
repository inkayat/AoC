def find_dest(c, p, x):
    # base case
    if x == '1':
        return c.index(max(c))
    if str(int(x)-1) in p:
        return find_dest(c, p, str(int(x)-1))
    return c.index(str(int(x)-1))


def update_order(p, d, c, index):
    """
        p: picked elements
        d: destination index
        c: cups list
    """
    order = c[:d]+[c[d]]+p+c[d+1:]
    if index>5:
        order = order[8-index:len(order)]+order[0:8-index]
    elif d<index:
        order = order[3:len(order)+1]+order[0:3]
    return order


def solve(c, n):
    _cups = [cup for cup in c]
    # mod
    m = len(_cups)
    for i in range(n):
        i %= m
        val = _cups[i]
        picked = _cups[i+1:i+4]+_cups[0:int(len(_cups)-i<=3)*(4+i-len(_cups))]
        _cups = _cups[int(len(_cups)-i<=3)*(4+i-len(_cups)):i+1]+_cups[i+4:len(_cups)]
        destination = find_dest(_cups, picked, val)
        _cups = update_order(picked, destination, _cups, i)
    return ''.join(_cups)


if __name__ == "__main__":
    cups = input()
    num_moves = int(input())
    solution = solve(cups, num_moves)
    print(solution)
