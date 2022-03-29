import pytest
from factorial import factorial


class Test:
    def test1(self):
        assert factorial(1) == 1

    def test2(self):
        assert factorial(3) == 6

    def test3(self):
        assert factorial(7) == 5040
