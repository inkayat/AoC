import math

class Loc:

    __directions__ = ['E', 'S', 'W', 'N']

    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = [0, 0]
        self.face = 0

    @property
    def loc(self):
        return [self.x, self.y]

    @loc.setter
    def loc(self, x, y):
        self.position = [x, y]

    @loc.getter
    def loc(self):
        return [self.x, self.y]

    def move(self, direction, value):
        if direction == 'N':
            self.y += value
        elif direction == 'S':
            self.y -= value
        elif direction == 'E':
            self.x += value
        elif direction == 'W':
            self.x -= value
        elif direction == 'R':
            self.face = (self.face + (value//90)) % 4
        elif direction == 'L':
            self.face = (self.face - (value//90)) % 4
        elif direction == 'F':
            self.move(self.__directions__[self.face], value)
        else:
            print("invalid direction")

    def manhattan_distance(self):
        return abs(self.x)+abs(self.y)

if __name__ == "__main__":

    loc = Loc()
    with open('../input.txt', 'r') as File:
        lines = File.readlines()
        for line in lines:
            d, v = line[0], int(line[1:])
            print(d, v)
            loc.move(d, v)
    print(loc.loc)
    print(loc.manhattan_distance())



