from random import randint


class GameMap:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.tiles = self.initialize_tiles()
        self.goals = []

    def initialize_tiles(self):
        tiles = [[100 for _ in range(self.width)] for _ in range(self.height)]
        return tiles

    def set_goals(self):
        for goal in range(0, 3):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.tiles[x][y] = 0
            self.goals.append((x, y))

    def dijkstra(self):
        changed = True
        while changed:
            changed = False
            for y in range(0, self.height):
                for x in range(0, self.width):
                    lowest_neighbor = self.get_lowest_neighbor_value(x, y)
                    if self.tiles[x][y] > lowest_neighbor + 1:
                        self.tiles[x][y] = lowest_neighbor + 1
                        changed = True

    def get_lowest_neighbor_value(self, x, y):
        lowest = 100
        if y > 0 and x > 0:
            lowest = min(lowest, self.tiles[x - 1][y - 1])
        if y > 0:
            lowest = min(lowest, self.tiles[x][y - 1])
        if x > 0:
            lowest = min(lowest, self.tiles[x - 1][y])
        if y < self.height - 1 and x < self.width - 1:
            lowest = min(lowest, self.tiles[x + 1][y + 1])
        if y < self.height - 1:
            lowest = min(lowest, self.tiles[x][y + 1])
        if x < self.width - 1:
            lowest = min(lowest, self.tiles[x + 1][y])
        return lowest

    def __repr__(self):
        out = ""
        for y in range(0, self.height):
            for x in range(0, self.width):
                out += str(hex(self.tiles[x][y])[2:])
            out += "\n"
        return out


if __name__ == '__main__':
    my_map = GameMap()
    my_map.set_goals()
    my_map.dijkstra()
    print(my_map)
