class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, Length, Width):
        self.length = Length
        self.width = Width

    def area(self):
        return self.length * self.width


Length = float(input("Enter the length of the rectangle: "))
Width = float(input("Enter the width of the rectangle: "))


Rectangle = Rectangle(Length, Width)


print("Answer:", Rectangle.area())
