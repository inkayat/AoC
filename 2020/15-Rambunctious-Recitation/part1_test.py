import pytest
from part1 import solve


def test_solve():
    assert solve([1,3,2], 2020) == 1
    assert solve([2,1,3], 2020) == 10
    assert solve([1,2,3], 2020) == 27
    assert solve([2,3,1], 2020) == 78
    assert solve([3,2,1], 2020) == 438
    assert solve([3,1,2], 2020) == 1836
