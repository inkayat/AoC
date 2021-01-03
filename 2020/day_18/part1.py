from functools import reduce
import re

INPUT_PATH = "../input.txt"

class Operation:

    def __init__(self):
        #sure these operations are sorted according to priority
        self.math_operations = ['+', '*']

    # worst complexity O(n), best complexity(1)
    def find_deepest_expression(self, expression):
        deepl = -1
        deepr = -1
        for i in range(len(expression)):
            if expression[i] == '(':
                deepl = i
            elif expression[i] == ')':
                deepr = i
            if deepl != -1 and deepr != -1:
                return deepl, deepr
        return deepl, deepr


    # complexity O(n), n is length of expression
    def operate(self, expression):
        """ Calculate given expression with only numbers and operations.
        """
        values = re.split('\*|\+', expression)
        left_value = int(values[0])
        index = len(values[0])
        for x in range(1, len(values)):
            if expression[index] == '+':
                left_value += int(values[x])
            elif expression[index] == '*':
                left_value *= int(values[x])
            else:
                print("Syntax error")
            index += len(values[x])+1
        return left_value

    # worst complextiy O(n^2), average O(n^2), best O(n)
    def evaluate(self, expression):
        l, r, result = -1, 0, -1

        _expression = expression
        while r!=-1:
            l, r = self.find_deepest_expression(_expression)
            if r!=-1:
                replaced_value = self.operate(_expression[l+1:r])
                _expression = _expression[:l]+str(replaced_value)+_expression[r+1:]

        return self.operate(_expression)


if __name__ == "__main__":
    #create Operation instance
    solver = Operation()
    cum_sum = 0
    #read input file line by line
    with open(INPUT_PATH) as File:
        lines = File.readlines()
    for line in lines:
        #preprocess
        clean_line = line.replace(' ', '')
        current_sum = solver.evaluate(clean_line)
        cum_sum+=current_sum

    #show result
    print(cum_sum)



