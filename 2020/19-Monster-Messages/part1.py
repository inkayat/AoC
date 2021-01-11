import re

global d

def solve(x):
    global d
    if all(not ('0' <= k <= '9') for k in d[x]):
        return d[x]
    t = d[x].split()
    for i in range(len(t)):
        if t[i] != '|' and t[i].isdigit():
            k = solve(t[i])
            d[x] = d[x].replace(' '+t[i]+ ' ', k)
    return d[x]


if __name__ == "__main__":
    global d
    d = dict()
    with open("input.txt") as fp:
        _input = fp.read()
        f = _input.split('\n\n')
        exp = f[0].split('\n')
        d = {i:' ( '+j.strip()+' ) ' for i, j in map(lambda x:x.split(':'), exp)}
    solve('0')
    d['0'] = d['0'].replace(' ', '')
    d['0'] = d['0'].replace('"a"', 'a')
    d['0'] = d['0'].replace('"b"', 'b')
    d['0'] = '^'+d['0']+'$'
    ans = 0
    for test in f[1].split('\n'):
        if re.match(d['0'], test):
            ans += 1
    print(ans)
