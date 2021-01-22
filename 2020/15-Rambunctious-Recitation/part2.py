from collections import defaultdict
from functools import lru_cache

def solve(numbers, n):
    current = -1
    memo = defaultdict(lambda:list())
    is_visited = defaultdict(lambda:0)
    for i in range(n):
        if i<len(numbers):
            current = numbers[i]
        else:
            if is_visited[current] == 1:
                current = 0
            else:
                current = (i)-memo[current][-2]
        is_visited[current] += 1
        memo[current].append(i+1)
        if len(memo[current]) > 2:
            memo[current] = memo[current][1:]
    return current

if __name__ == "__main__":
    puzzle_input = input("numbers: ")
    n = int(input("nth: "))
    numbers = list(map(int, puzzle_input.split(",")))
    nth_spoken = solve(numbers, n)
    print(nth_spoken)

