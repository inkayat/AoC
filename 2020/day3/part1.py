class Solution:
    """solution"""
    def __init__(self, grid):
        self.grid = grid
        self.number_of_trees = 0
        self.nrows = len(grid)
        self.ncols = len(grid[0])

    def find_ntrees(self):
        for i in range(1, self.nrows):
            if self.grid[i][3*i] == "#":
                self.number_of_trees += 1
        return self.number_of_trees


if __name__ == "__main__":
    # actual list
    grid = list()
    # read input.txt
    with open("input.txt", "r") as File:
        ss = File.read()
    # make list from input string splitting by "\n"
    grid = ss.split("\n")
    # make sure you reach most bottom row before the right most column
    safemul = 3*len(grid)//len(grid[0])+1
    # temp list
    new_grid = list()
    # create actual grid what exactly looks like given description
    for line in grid:
        new_grid.append([i for i in line*safemul])
    # preprocessing: last list is empty, ignore it
    grid = new_grid[:-1]
    # create Solution class and call necessary method to find answer
    result = Solution(grid).find_ntrees()
    # show answer
    print(result)
