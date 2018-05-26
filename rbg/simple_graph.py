class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, value):
        return self.edges[value]


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    @staticmethod
    def from_id_width(value, width):
        return value % width, value // width

    def in_bounds(self, value):
        (x, y) = value
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, value):
        return value not in self.walls

    def neighbors(self, value):
        (x, y) = value
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y-1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
