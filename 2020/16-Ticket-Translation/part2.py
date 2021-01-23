from typing import List, Dict, Set
from collections import defaultdict
import re

def check_validation(ticket: List, ranges: Dict[str, List[Set]]):
    for i in ticket:
        is_ok = False
        for key in ranges:
            if i in range(int(ranges[key][0][0]), int(ranges[key][0][1])+1) \
                    or i in range(int(ranges[key][1][0]), int(ranges[key][1][1])+1):
                is_ok = True
        if not is_ok:
            return False
    return is_ok

if __name__ == "__main__":
    my_ticket = [113,53,97,59,139,73,89,109,67,71,79,127,149,107,137,83,131,101,61,103]
    with open('input.txt') as fp:
        lines = fp.readlines()
        ranges = {}
        positions = {}
        ss = defaultdict(lambda:set())
        visited = defaultdict(lambda:False)
        for i in range(20):
            nums = re.findall('(\d+)-(\d+)', lines[i])
            key = re.findall('(.*):', lines[i])
            ss[key[0]] = set()
            positions[key[0]] = -1
            ranges[key[0]] = nums
        ans = 0
        final_list = list()
        for i in range(25, len(lines)):
            nearby_ticket = list(map(int, lines[i].strip('\n').split(',')))
            if check_validation(nearby_ticket, ranges):
                final_list.append(nearby_ticket)
        final_list.append(my_ticket)
        indexes = defaultdict(lambda:[])
        for i in range(len(final_list)):
            for j in range(20):
                indexes[j].append(final_list[i][j])
        for key in indexes:
            for rang in ranges:
                is_ok = True
                for num in indexes[key]:
                    if int(num) in range(int(ranges[rang][0][0]), int(ranges[rang][0][1])+1) \
                            or int(num) in range(int(ranges[rang][1][0]), int(ranges[rang][1][1])+1):
                        continue
                    else:
                        is_ok = False
                        break
                if is_ok:
                    ss[rang].add(key)
        keypos = []
        for key in ss:
            keypos.append([key, ss[key]])
        keypos.sort(key=lambda x: len(x[1]))
        for key, pos in keypos:
            for i in pos:
                if not visited[i]:
                    visited[i] = True
                    positions[key] = i
                    break

    d_1 = my_ticket[positions['departure location']]
    d_2 = my_ticket[positions['departure station']]
    d_3 = my_ticket[positions['departure platform']]
    d_4 = my_ticket[positions['departure track']]
    d_5 = my_ticket[positions['departure date']]
    d_6 = my_ticket[positions['departure time']]
    ans = d_1 * d_2 * d_3 * d_4 * d_5 * d_6
    print(ans)