from rbg.simple_graph import SimpleGraph, SquareGrid
from rbg.queue import Queue


def breadth_first_search_1(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {start: True}

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                frontier.put(neighbor)
                visited[neighbor] = True


def breadth_first_search_2(graph, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()
        for neighbor in graph.neighbors(current):
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current

    return came_from


def draw_tile(graph, value, style, width):
    r = "."
    if 'number' in style and value in style['number']:
        r = "%d" % style['number'][value]
    if 'point_to' in style and style['point_to'].get(value, None) is not None:
        (x1, y1) = value
        (x2, y2) = style['point_to'][value]
        if x2 == x1 + 1:
            r = ">"
        if x2 == x1 - 1:
            r = "<"
        if y2 == y1 + 1:
            r = "v"
        if y2 == y1 - 1:
            r = "^"
    if 'start' in style and value == style['start']:
        r = "A"
    if 'goal' in style and value == style['goal']:
        r = "Z"
    if 'path' in style and value in style['path']:
        r = "@"
    if value in graph.walls:
        r = "#" * width
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


if __name__ == '__main__':
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    # breadth_first_search_1(example_graph, 'A')

    DIAGRAM1_WALLS = []
    for val in [21, 22, 51, 52, 81, 82, 93, 94, 111, 112, 123, 124, 133, 134, 141, 142, 153, 154, 163, 164, 171, 172,
                173, 174, 175, 183, 184, 193, 194, 201, 202, 203, 204, 205, 213, 214, 223, 224, 243, 244, 253, 254,
                273, 274, 283, 284, 303, 304, 313, 314, 333, 334, 343, 344, 373, 374, 403, 404, 433, 434]:
        DIAGRAM1_WALLS.append(SquareGrid.from_id_width(val, width=30))
    g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS
    # draw_grid(g)

    parents = breadth_first_search_2(g, (8, 7))
    draw_grid(g, width=2, point_to=parents, start=(8, 7))
