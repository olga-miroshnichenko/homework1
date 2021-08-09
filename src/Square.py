from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Square'

    def __init__(self, height: int):
        super().__init__(height, height)
