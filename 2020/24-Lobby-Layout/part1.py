from collections import defaultdict

def solve(lines):
    d = {'e':[-1, 0], 'se':[-0.5, -0.5], 'sw':[0.5, -0.5], 'w':[1, 0], 'nw':[0.5, 0.5], 'ne':[-0.5,0.5]}
    ans = 0
    tiles = defaultdict(lambda:defaultdict(lambda:0))
    for line in lines:
        line = line.strip('\n')
        i = 0
        coord = [0,0]
        while i < len(line):
            if i == len(line)-1:
                coord[0] += d[line[i]][0]
                coord[1] += d[line[i]][1]
            else:
                if line[i:i+2] in d:
                    coord[0] += d[line[i:i+2]][0]
                    coord[1] += d[line[i:i+2]][1]
                    i+=1
                else:
                    coord[0] += d[line[i]][0]
                    coord[1] += d[line[i]][1]
            i+=1
        tiles[coord[0]][coord[1]] += 1
    for key in tiles:
        for val in tiles[key]:
            ans += tiles[key][val]%2
    return ans


if __name__ == "__main__":
    with open('input.txt') as fp:
        lines = fp.readlines()
        black = solve(lines)
        print(black)
