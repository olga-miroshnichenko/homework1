import pytest

from src.Square import Square


def test_calc_area():
    square = Square(2)
    square.calc_area()
    assert square.area == 4


def test_calc_perimeter():
    square = Square(2)
    square.calc_perimeter()
    assert square.perimeter == 8

