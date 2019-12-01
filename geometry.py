"""
This is a geometry module that adds classes and functions in the field of geometry, including coordinates, planes, etc.
"""


class Plane:
    """
    Geometry plane to store, create and handle shapes, coordinates and all geometry elements
    """
    all_coordinates = []
    all_shapes = []

    def __init__(self, max_x=255, min_x=-255, max_y=255, min_y=-255):
        """
        :param max_x:
        :param min_x:
        :param max_y:
        :param min_y:
        """
        self.max_x = max_x
        self.mim_x = min_x
        self.max_y = max_y
        self.min_y = min_y
        self.coordinates = []
        self.coordinates_1 = []
        self.coordinates_2 = []
        self.coordinates_3 = []
        self.coordinates_4 = []
        self.coordinates_0 = []
        self.coordinates__1 = []
        self.shapes = []

    def new_coordinate(self, x, y):
        coordinate = Coordinate(x, y)
        self.coordinates.append(coordinate)
        self.coordinates.append((x, y))
        self.all_coordinates.append(coordinate)
        self.all_coordinates.append((x, y))
        if coordinate.quadrant == 1:
            self.coordinates_1.append((coordinate, (x, y)))
        elif coordinate.quadrant == 2:
            self.coordinates_2.append((coordinate, (x, y)))
        elif coordinate.quadrant == 3:
            self.coordinates_3.append((coordinate, (x, y)))
        elif coordinate.quadrant == 4:
            self.coordinates_4.append((coordinate, (x, y)))
        elif coordinate.quadrant == 0:
            self.coordinates_0.append((coordinate, (x, y)))
        elif coordinate.quadrant == -1:
            self.coordinates__1.append((coordinate, (x, y)))
        return coordinate

    def new_shape(self, *args):
        shape = Shape(args)
        self.shapes.append(shape)
        self.all_shapes.append(shape)


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.quadrant = -2
        if x > 0 and y > 0:
            self.quadrant = 1
        elif x < 0 < y:
            self.quadrant = 2
        elif x < 0 and y < 0:
            self.quadrant = 3
        elif x > 0 > y:
            self.quadrant = 4
        elif x == 0 and y == 0:
            self.quadrant = 0
        else:
            self.quadrant = -1

    def get_distance(self, other, hipot=False):
        difference_x = other.x - self.x
        difference_y = other.y - self.y
        if hipot:
            return (difference_x, difference_y,)
        return (difference_x, difference_y)


class Shape:

    def __init__(self, *args):
        self.width = 0
        self.height = 0
        self.corners = []
        self.angles = []
        self.edges = []
        for corner in args:
            self.corners.append(corner)
            if args.index(corner) > 0:
                self.edges.append((args[args.index(corner) - 1], corner))
        self.edges.append((args[args.__sizeof__() - 1], args[0]))


class Square(Shape):
    side = 0

    def __init__(self, c0, side):
        try:
            self.corners.append(c0)
        except ValueError:
            print("Side isn't an integer number")
            raise
        x0, y0 = c0
        self.side = side
        try:
            self.corners.append((x0 + int(side), y0))
            self.corners.append((x0 + int(side), y0 + int(side)))
            self.corners.append((x0, y0 + int(side)))
        except ValueError:
            print("Side isn't an integer number")
            raise
