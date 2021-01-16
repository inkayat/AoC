from collections import defaultdict
import re

def solve(mask, value):
    value = bin(int(value))[2:]
    value = '0'*(len(mask)-len(value))+value
    result = ''.join([i if j == 'X' else j for i, j in zip(value, mask)])
    return result


if __name__ == "__main__":
    with open('input.txt') as fp:
        lines = fp.readlines()
    memo = defaultdict(lambda:False)
    for line in lines:
        if re.search('^mask = ', line):
            mask = re.findall('^mask = (.*)', line)[0]
        else:
            _key = re.findall('mem\[(\d+)\]', line)[0]
            value = re.findall('= (\d+)\n', line)[0]
            result = solve(mask, value)
            memo[_key] = result
    _sum = sum([int(memo[i], 2) for i in memo])
    print(_sum)
