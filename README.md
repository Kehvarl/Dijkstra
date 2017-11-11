# Dijkstra
Quick toy to play with Dijkstra Maps for Roguelikes

## Based on the Dijkstra articles on Rogue Basin
http://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps

http://www.roguebasin.com/index.php?title=Dijkstra

To use:
```python
from dijkstra_map import DijkstraMap
my_map = DijkstraMap(30, 10)
my_map.add_goal(5, 5)
my_map.add_goal(8, 5, -3) #Apply a weight for a goal, lower is more desirable
my_map.recalculate_map()
print(my_map) # Display the map weights 1-number per tile
for move in my_map.get_move_options(3, 3): # Get the recommended moves from a location on the map
    print(move)
```
