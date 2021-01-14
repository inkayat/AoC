from collections import defaultdict, deque
from typing import List, Dict
import re

global holder
global inst
global changes


def solve(ins):
    index, acc = 0, 0
    while index < len(ins):
        if ins[index][0] == 'nop':
            index += 1
        elif ins[index][0] == 'jmp':
            index += ins[index][1]
        else:
            acc += ins[index][1]
            index += 1
    return acc


def find(ins: List[str], visited, index, change) -> int:
    if index >= len(ins):
        return True
    if visited[index]:
        return False
    else:
        visited[index] = True
        if change == index:
            if ins[change][0] == 'nop':
                ins[change] = ['jmp', ins[change][1]]
            elif ins[change][0] == 'jmp':
                ins[change] = ['nop', ins[change][1]]
        if ins[index][0] == 'nop':
            return find(ins, visited, index+1, change)
        elif ins[index][0] == 'jmp':
            return find(ins, visited, index+ins[index][1], change)
        else:
            return find(ins, visited, index+1, change)


if __name__ == "__main__":
    changes = defaultdict(lambda:False)
    visited = defaultdict(lambda:False)
    with open("input.txt") as fp:
        lines = fp.readlines()
        inst = []
        for line in lines:
            instruction = re.findall(r'([a-z]+)\s', line)[0]
            offset = int(re.findall(r'([+-][0-9]+)\n', line)[0])
            inst.append([instruction, offset])
    holder = []
    for i in range(len(inst)):
        if inst[i][0] in ('jmp', 'nop'):
            holder.append(i)
    change = -1
    for i in holder:
        if find(inst.copy(), visited.copy(), 0, i):
            change = i
            break
    if inst[change][0] == 'jmp':
        inst[change] = ['nop', inst[change][1]]
    elif inst[change][0] == 'nop':
        inst[change] = ['jmp', inst[change][1]]
    acc = solve(inst)
    print(acc)

