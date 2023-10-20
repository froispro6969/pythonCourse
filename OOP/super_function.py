# super() = function used to give access to the methods of a parent class. Return a temporary object of a parent class when ued


class Rectange:

    def __init__(self, length, width):
        self.length = length
        self.width = width



class Square(Rectange):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectange):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())
