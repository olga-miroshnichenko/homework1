import pytest

from src.Circle import Circle


def test_calc_area():
    circle = Circle(2)
    circle.calc_area()
    assert circle.area == 12.56


def test_calc_perimeter():
    circle = Circle(2)
    circle.calc_perimeter()
    assert circle.perimeter == 12.56
