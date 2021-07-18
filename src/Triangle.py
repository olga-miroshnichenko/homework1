from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, side_1: int, side_2: int, side_3: int):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if not self.can_create(side_1, side_2, side_3):
            raise ValueError('Передан неверный аргумент.')

    def calc_area(self):
        self.calc_perimeter()
        halfPerimeter = self.perimeter / 2
        self.area = sqrt(halfPerimeter * (halfPerimeter - self.side_1) *
                         (halfPerimeter - self.side_2) * (halfPerimeter - self.side_3))

    def calc_perimeter(self):
        self.perimeter = self.side_1 + self.side_2 + self.side_3

    @staticmethod
    def can_create(a, b, c) -> bool:
        return a + b > c and a + c > b and b + c > a

