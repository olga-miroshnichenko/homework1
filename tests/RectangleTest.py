import pytest

from src.Rectangle import Rectangle


def test_calc_area():
    rect = Rectangle(2, 2)
    rect.calc_area()
    assert rect.area == 4


def test_calc_perimeter():
    rect = Rectangle(2, 2)
    rect.calc_perimeter()
    assert rect.perimeter == 8
