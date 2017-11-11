class DijkstraMap:
    """
    Python implementation of Dijkstra Maps
    Source: http://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps
            http://www.roguebasin.com/index.php?title=Dijkstra
    """

    # X, Y Transitions to the 8 neighboring cells
    neighbors = [(-1, -1), (0, -1), (1, -1),
                 (-1, 0), (1, 0),
                 (-1, 1), (0, 1), (1, 1)]

    def __init__(self, width, height):
        """
        Create a Map  showing the movement score of various tiles
        :param int width: Map size in tiles
        :param int height: Map size in tiles
        """
        self.width = width
        self.height = height
        self.goals = []
        self.tiles = []
        self._clear_map()

    def add_goal(self, x, y, score=0):
        """
        Add a goal tile to the map
        :param int x: Tile X coordinate
        :param int y: Tile Y coordinate
        :param int score: Desirability of this location (default: 0)
        """
        self.goals.append((x, y, score))

    def recalculate_map(self):
        """
        Use Dijkstra's Algorithm to calculate the movement score towards
        goals in this map
        """
        self._clear_map()
        changed = True
        while changed:
            changed = False
            for y in range(0, self.height):
                for x in range(0, self.width):
                    lowest_neighbor = self._get_lowest_neighbor_value(x, y)
                    if self.tiles[x][y] > lowest_neighbor + 1:
                        self.tiles[x][y] = lowest_neighbor + 1
                        changed = True

    def get_move_options(self, x, y):
        """
        Return a list of ideal moves from a given point
        :param x: Entity X Coordinate
        :param y: Entity Y Coordinate
        :return list: Recommended moves
        """
        best = self._get_lowest_neighbor_value(x, y)
        moves = []
        for dx, dy in DijkstraMap.neighbors:
            tx, ty = x + dx, y + dy
            if self.point_in_map(tx, ty) and self.tiles[tx][ty] == best:
                moves.append({'move': (dx, dy)})
        return moves

    def point_in_map(self, x, y):
        """
        Checks if a given point falls within the current map
        :param x: Target X position
        :param y: Target Y position
        :return: True if desired location is within map bounds
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def _clear_map(self, default=10):
        """
        Reset the map scores to an arbitrary value and populate goals
        :param int default: the initial value to set for each cell
        """
        self.tiles = [
            [default
             for _ in range(self.height)]
            for _ in range(self.width)]

        for (x, y, score) in self.goals:
            self.tiles[x][y] = score

    def _get_lowest_neighbor_value(self, x, y):
        """
        Get the score in the current lowest-valued neighbor cell
        :param x: Current X Coordinate
        :param y: Current Y Coordinate
        :return int: Lowest neighboring value
        """
        lowest = 100
        for dx, dy in DijkstraMap.neighbors:
            tx, ty = x + dx, y + dy
            if self.point_in_map(tx, ty):
                lowest = min(lowest, self.tiles[tx][ty])
        return lowest

    def __repr__(self):
        """
        Output the current map in a printable fashion
        :return string: Printable form of map
        """
        out = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                out += str(hex(self.tiles[x][y])[2:])
            out += "\n"
        return out
