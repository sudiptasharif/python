class Coordinate(object):
    """
    Simulates a 2D Coordinate Point.
    Initialize object using int x and y values.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


p = Coordinate(3, 4)
o = Coordinate(0, 0)
print(p)
print(p.x)
print(p.y)   

print("Origin x = " + str(o.x))
print("Origin y = " + str(o.y))

distance = p.distance(o)
print(distance)

print(Coordinate.distance(p, o))

print(o)

print(type(p))
print(type(Coordinate))

print(type(2))
print(type("s"))

print(isinstance(p, Coordinate))
print(isinstance(p, str))
