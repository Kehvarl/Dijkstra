from rbg.simple_graph import SimpleGraph, SquareGrid, WeightedSquareGrid
from rbg.queue import Queue, PriorityQueue


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


def breadth_first_search_2(graph, start, goal=None):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        if goal is not None and current == goal:
                break

        for neighbor in graph.neighbors(current):
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current

    return came_from


def dijkstra_search(graph, start, goal=None):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if goal is not None and current == goal:
                break

        for neighbor in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


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

#    parents = breadth_first_search_2(g, (8, 7))
#    draw_grid(g, width=2, point_to=parents, start=(8, 7), goal=(17, 2))

    diagram4 = WeightedSquareGrid(10, 10)
    diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
    # diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
    #                                       (4, 3), (4, 4), (4, 5), (4, 6),
    #                                       (4, 7), (4, 8), (5, 1), (5, 2),
    #                                       (5, 3), (5, 4), (5, 5), (5, 6),
    #                                       (5, 7), (5, 8), (6, 2), (6, 3),
    #                                       (6, 4), (6, 5), (6, 6), (6, 7),
    #                                       (7, 3), (7, 4), (7, 5)]}

    origin, cost = dijkstra_search(diagram4, (1, 4))
    draw_grid(diagram4, width=3, point_to=origin, start=(1, 4), goal=(7, 8))
    print()
    draw_grid(diagram4, width=3, number=cost, start=(1, 4), goal=(7, 8))
#    print()
#    draw_grid(diagram4, width=3, path=reconstruct_path(origin, start=(1, 4), goal=(7, 8)))
