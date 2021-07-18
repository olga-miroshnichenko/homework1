import pytest

from src.Circle import Circle
from src.Square import Square

def test_error_if_not_isinstance_figure():
   with pytest.raises(ValueError):
       circle = Circle(10)

       class A:
           pass

       a = A()

       circle.add_area(a)


def test_correct_sum_area():
    c = Circle(10)
    s = Square(5)

    c.add_area(s)
    assert c.add_area(s) == 25
