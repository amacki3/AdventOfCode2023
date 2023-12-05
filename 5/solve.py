import os 
import re
from bisect import bisect

class router:
    def __init__(self,destination,source,range_value):
        self.source = source
        self.destination = destination
        self.range_value = range_value
        
    def apply(self,val):
        return val + (self.destination-self.source)

def solve_part1(input):
    result = 0

    maps = [[] for i in range(7)] #7 is num of maps
    mapIndex = -1
    #we dont have to worry about the routing of the maps, as they are linear and pre-sorted

    for line in input:
        if line.startswith("seeds:"):
            line = line.strip("seeds: ")
            seeds = [int(num) for num in line.split()]
        elif line[0].isdigit():
            nums = line.split()
            maps[int((mapIndex-1)/2)].append(router(int(nums[0]),int(nums[1]),int(nums[2])))
            #Could do better with the mapindex, but this works so meh
        else:
            mapIndex += 1

    for index,routes in enumerate(maps):
        maps[index] = sorted(routes,key=lambda x: x.source)

    minLocation = -1
    for seed in seeds:
        #we iterate through our routes and apply them
        #each set of routes is in order now, so we can simply find the first one
        #which has a source above our seed and check if the last ones range fits.
        #We use pyhton built in bisect, which is effectively a binary search alg.
        for routes in maps:
            routeid = bisect(routes,seed, key=lambda x: x.source) -1
            if routeid > -1 and (routes[routeid].source + routes[routeid].range_value) >= seed:
                seed = routes[routeid].apply(seed)
            else:
                seed = seed
        if minLocation > seed or minLocation == -1:
            minLocation = seed

    return minLocation
        


def solve_part2(input):
    result = 0
    return result

if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 1")
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 2")
        print(solve_part2(input))
        