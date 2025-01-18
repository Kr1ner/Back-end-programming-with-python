import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        v1, v2, v3 = self.__vertices
        return (
            v1.distance_from_point(v2) +
            v2.distance_from_point(v3) +
            v3.distance_from_point(v1)
        )

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())