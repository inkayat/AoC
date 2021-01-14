from collections import defaultdict
from typing import List, Dict
import re

def solve(instructions: List[str], visited: defaultdict) -> int:
    index = 0
    acc = 0
    while not visited[index]:
        instruction = re.findall(r'([a-z]+)\s', instructions[index])[0]
        offset = int(re.findall(r'([+-][0-9]+)\n', instructions[index])[0])
        visited[index] = True
        if instruction == 'nop':
            index += 1
            continue
        elif instruction == 'jmp':
            index += offset
        elif instruction == 'acc':
            acc += offset
            index += 1
    return acc


if __name__ == "__main__":
    with open("input.txt") as fp:
        lines = fp.readlines()
    visited = defaultdict(lambda:False)
    ans = solve(lines, visited)
    print(ans)
