from typing import List
from collections import defaultdict

def solve(arr: List[int], n: int) -> int:
    """n-number preamble
    """
    d = defaultdict(lambda:-1)
    d = {arr[i]:True for i in range(n)}
    for i in range(n, len(arr)):
        for key in d:
            is_found = False
            if arr[i]-key in d:
                del d[arr[i-n]]
                d[arr[i]] = True
                is_found = True
                break
        if not is_found: return arr[i]
    return -1


if __name__ == "__main__":
    numbers = List[int]
    with open('input.txt') as fp:
        _input = fp.read()
    numbers = list(map(int, _input.strip('\n').split('\n')))
    print(solve(numbers, 25))
