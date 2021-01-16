from collections import defaultdict
import re

if __name__ == "__main__":
    with open("input.txt") as fp:
        lines = fp.readlines()
        d = defaultdict(lambda:set())
        ingredients = defaultdict(lambda:0)
        ingredient_list = list()
        for line in lines:
            ing = re.findall('(.*)\(', line)[0].strip().split()
            ingredient_list.append(ing)
            con = re.findall('contains\s(.*)\)', line.replace(',', ''))[0].split()
            for i in ing:
                ingredients[i] += 1
            for c in con:
                if len(d[c]) == 0:
                    d[c] = set(ing)
                else:
                    d[c] &= set(ing)
        _all = set()
        for s in d:
            _all |= d[s]
        result = 0
        for ingredient in ingredient_list:
            result += len([i for i in ingredient if i not in _all])
        print(result)
