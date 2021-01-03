import pytest
from day18p1 import Operation

def test_without_parentheses():
    solver = Operation()
    assert solver.evaluate("1 + 2 * 3 + 4 * 5 + 6") == 71

def test_with_parentheses():
    solver = Operation()
    assert solver.evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert solver.evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert solver.evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
