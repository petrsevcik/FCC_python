class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return self.height*(self.width*"*" + "\n")

    def get_amount_inside(self, object):
        return int(self.get_area() / object.get_area())

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        return f"Square(side={self.height})"
# Additionally, the set_width and set_height methods on the Square class should set both the width and height.
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))