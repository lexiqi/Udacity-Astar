from helpers import Map, load_map, show_map
from helper import Maps, load_maps, show_maps
from student_code import shortest_path
from student_code import Astar
map_40 = load_map('map-40.pickle')
#show_map(map_40, start=5, goal=34, path=[5,16,37,12,34])
#print(map_40.intersections)
#print(map_10.roads)

pathList=shortest_path(map_40,start=5,goal=34)
print(pathList)