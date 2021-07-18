from src.Square import Square
from src.Circle import Circle

c = Circle(10)
s = Square(5)

s.add_area(c)


class A:
    pass


a = A()

c.add_area(a)
