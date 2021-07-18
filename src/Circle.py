from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius: int):
        self.radius = radius

    def calc_area(self):
        self.area = 3.14 * self.radius ** 2

    def calc_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
