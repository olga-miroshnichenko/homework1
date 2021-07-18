from src.Figure import Figure


class Rectangle(Figure):

    name = 'Rectangle'

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def calc_area(self):
        self.area = self.height * self.width

    def calc_perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
