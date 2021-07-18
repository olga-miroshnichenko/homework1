from abc import ABC, abstractmethod


class Figure(ABC):
    name: str
    area = 0
    perimeter = 0

    @abstractmethod
    def calc_area(self) -> float:
        pass

    @abstractmethod
    def calc_perimeter(self) -> float:
        pass

    def add_area(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError('Передан неправильный класс.')
        else:
            figure.calc_area()
            return figure.area + self.area
