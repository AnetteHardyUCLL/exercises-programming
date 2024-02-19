from math import pi


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def perimeter(self):
        return 2 * pi * self.radius

    @property
    def area(self):
        return pi * self.radius ** 2
