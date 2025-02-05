class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, Length):
        self.length = Length

    def area(self):
        return self.length * self.length


Length = float(input())


square = Square(Length)


print(square.area())
