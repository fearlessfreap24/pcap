import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x: int, y: int):
        dif_x = self.__x - x
        dif_y = self.__y - y
        return math.hypot(dif_x, dif_y)

    def distance_from_point(self, point):
        dif_x = self.__x - point.getx()
        dif_y = self.__y - point.gety()
        return math.hypot(dif_x, dif_y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vert1 = vertice1
        self.__vert2 = vertice2
        self.__vert3 = vertice3

    def perimeter(self):
        leg1 = self.__vert1.distance_from_point(self.__vert2)
        leg2 = self.__vert2.distance_from_point(self.__vert3)
        leg3 = self.__vert3.distance_from_point(self.__vert1)
        return leg1 + leg2 + leg3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
