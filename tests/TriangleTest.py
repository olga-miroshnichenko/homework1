import pytest

from src.Triangle import Triangle


def test_calc_area():
    tria = Triangle(2, 2, 2)
    tria.calc_area()
    assert round(tria.area, 2) == 1.73


def test_calc_perimeter():
    tria = Triangle(2, 2, 2)
    tria.calc_perimeter()
    assert tria.perimeter == 6


def test_error_invalid_arguments():
    with pytest.raises(ValueError):
        Triangle(2, -1, 2)
