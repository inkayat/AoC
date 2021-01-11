from typing import List

def solve(answer: List[str]) -> int:
    return sum([len(set(k for k in ans)) for ans in answer])


if __name__ == "__main__":
    with open('input.txt') as fp:
        text = fp.read()
    answers = list(map(lambda x:x.replace('\n', ''), text.split('\n\n')))
    print(solve(answers))
