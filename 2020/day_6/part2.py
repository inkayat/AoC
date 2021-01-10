from functools import reduce

def solve(answer):
    return sum([len(reduce(lambda x, y: set(x)&set(y), l.strip('\n').split('\n'))) for l in answers])


if __name__ == "__main__":
    with open('input.txt') as fp:
        text = fp.read()
    answers = list(text.split('\n\n'))
    print(solve(answers))
