import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The point is located in ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x1 = float(input("Enter the x coordinate for the first point: "))
y1 = float(input("Enter the y coordinate for the first point: "))
point1 = Point(x1, y1)

x2 = float(input("Enter the x coordinate for the second point: "))
y2 = float(input("Enter the y coordinate for the second point: "))
point2 = Point(x2, y2)

print("\coordinates of the entered points:")
point1.show()
point2.show()

distance = point1.dist(point2)
print("\distance between points:", distance)
