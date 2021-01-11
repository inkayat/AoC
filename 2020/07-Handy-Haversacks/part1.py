from typing import List, Text
import re


def solve(bag, table: List[Text], selected):
    if len(table[bag]) == 0:
        return False
    if selected in table[bag]:
        return True
    ans = False
    for bg in table[bag]:
        if table[bag][bg] != 0:
            ans |= solve(bg, table, selected)
    return ans


if __name__ == "__main__":
    table = dict(dict())
    with open('input.txt') as fp:
        lines = fp.readlines()
        for line in lines:
            pattern = "\d+\s([a-z\s]+)\sbags?"
            pattern_num = "(\d+)\s"
            founded = re.findall(pattern, line)
            nums = re.findall(pattern_num, line)
            key = re.findall('^(.*)\sbags\scontain', line)
            if len(key) == 1:
                x = key[0]
                table[x] = {}
            if len(founded) > 0:
                for bag, num in zip(founded,nums):
                    table[x][bag] = int(num)
    ans = 0
    selected = 'shiny gold'
    for bag in table:
        if bag != selected:
            if solve(bag, table, selected):
                ans += 1
    print(ans)


