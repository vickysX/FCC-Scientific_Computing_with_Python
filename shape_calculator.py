import math

class Rectangle:
    def __init__(self, base, altezza):
        self.width = base
        self.heigth = altezza
    def set_heigth(self, altezza):
        self.heigth = altezza
    def set_width(self, base):
        self.width = base
    def get_area(self):
        return self.width * self.heigth
    def get_perimeter(self):
        return 2 * self.width + 2 * self.heigth
    def get_diagonal(self):
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.heigth, 2))
    def get_picture(self):
        if self.width > 50 or self.heigth > 50:
            return "Too big for picture."
        picture = ''''''
        for i in range(0, self.heigth):
            for j in range(0, self.width):
                picture += '*'
            picture += '\n'
        return picture
    def get_amount_inside(self, shape):
        ratio = int(self.get_area() / shape.get_area())
        return ratio
    def __repr__(self):
        return f"Rectangle(width={self.width}, heigth={self.heigth})"
    def __str__(self):
        return self.__repr__()

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.heigth = side
    def set_side(self, side):
        self.width = side
        self.heigth = side
    def set_heigth(self, altezza):
        self.set_side(altezza)
    def set_width(self, base):
        self.set_side(base)
    def __repr__(self):
        return f"Square(side={self.width})"
    def __str__(self):
        return self.__repr__()

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_heigth(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_heigth(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
