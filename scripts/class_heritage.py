class Rectangle(object):
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width
        self.__name = "rectangle"

    def perimeter(self):
        return f"{(self.__length + self.__width)*2}"

    def surface(self):
        return f"{self.__length*self.__width}"

    def show_detail(self):
        print(f"A {self.__name} of length {self.__length} and width {self.__width}")
        print(f"Its surface is {self.surface()}")
        print(f"Its perimeter is {self.perimeter()}")


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.__name = "square"


if __name__ == '__main__':
    objectRectangle = Rectangle(10, 20)
    objectRectangle.show_detail()
    objectSquare = Square(5)
    objectSquare.show_detail()
