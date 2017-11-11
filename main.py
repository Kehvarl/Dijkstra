from dijkstra_map import DijkstraMap
from random import randint


def set_goals(map, num_goals=3):
    """

    :param DijkstraMap map: The map needing goals
    :param int num_goals: Number of goals to add
    :return:
    """
    for goal in range(0, num_goals):
        x = randint(0, map.width - 1)
        y = randint(0, map.height - 1)
        map.add_goal(x, y)


if __name__ == '__main__':
    my_map = DijkstraMap(30, 10)
    set_goals(my_map, 3)
    my_map.recalculate_map()
    print(my_map)
    for move in my_map.get_move_options(3, 3):
        print(move)
