class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def circum(self):
        c = 2 * self.radius * self.pi
        print(f"Circumference of the Circle: {c}")

    def area(self):
        area = self.pi * self.radius * self.radius
        print(f"Area of the circle: {area:.2f}")


c_1 = Circle(3)
c_1.circum()
c_1.area()