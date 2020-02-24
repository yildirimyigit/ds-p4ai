from math import sqrt, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.length = self.start.distance(self.end)

    def set_start(self, n_start):
        self.start = n_start

    def __ge__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length


class Shape:
    def circumference(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def circumference(self):
        return 2 * self.radius * pi

    def area(self):
        return pi * self.radius**2


class Triangle(Shape):
    def __init__(self, corners):
        if len(corners) == 3 and all([type(c) == Point for c in corners]):
            self.corners = corners
            self.sides = [Line(corners[0], corners[1]),
                          Line(corners[0], corners[2]),
                          Line(corners[1], corners[2])]
        elif len(corners) == 6:
            self.corners = [Point(corners[0], corners[1]),
                            Point(corners[2], corners[3]),
                            Point(corners[4], corners[5])]
            self.sides = [Line(self.corners[0], self.corners[1]),
                          Line(self.corners[0], self.corners[2]),
                          Line(self.corners[1], self.corners[2])]

    def circumference(self):
        return sum([side.length for side in self.sides])

    # Herons Area Formula area = √(s * (s - a) * (s - b) * (s - c))
    def area(self):
        # Herons Area Formula area = √(s * (s - a) * (s - b) * (s - c))
        s_circ = self.circumference() / 2
        return sqrt(s_circ * (s_circ - self.sides[0].length) * (s_circ - self.sides[1].length) * (s_circ - self.sides[2].length))


triangle1 = Triangle([0, 0, 3, 0, 0, 4])
print(triangle1.circumference())
print(triangle1.area())


class RightTriangle(Triangle):

    def __init__(self, corners):
        super(RightTriangle, self).__init__(corners)

        self.sides = sorted(self.sides)
        if self.sides[0].length**2 + self.sides[1].length**2 != self.sides[2].length**2:
            raise NotRightTriangle

    def area(self):
        return self.sides[0].length * self.sides[1].length / 2


class NotRightTriangle(Exception):
    def __init__(self):
        self.args = ('Not a Right Triangle',)


right_triangle = RightTriangle([Point(0, 0), Point(3, 0), Point(0, 4)])
print(right_triangle.circumference())
print(right_triangle.area())

# Not a right Triangle!
try:
    RightTriangle([Point(0, 0), Point(4, 0), Point(0, 4)])
except NotRightTriangle as e:
    print(e.args[0])
    print('Given Points does not form a Right Triangle')

print("???")








