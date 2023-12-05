import os 
import re
from bisect import bisect_left
import numpy as np

class router:
    def __init__(self,destination,source,range_value):
        self.source = np.int64(source)
        self.destination = np.int64(destination)
        self.range_value = np.int64(range_value)
        
    def apply(self,val):
        return val + (self.destination-self.source)

def parse_input(input):
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
    return seeds,maps



def determine_min_location(seeds,maps):
    minLocation = -1
    new_seeds = np.array(seeds,dtype=np.int64)
    #we iterate through our routes and apply them
    #each set of routes is in order now, so we can simply find the first one
    #which has a source above our seed and check if the last ones range fits.
    #We use pyhton built in bisect, which is effectively a binary search alg.
    #For each route we find if any seeds are appropriate and then route it before moving on.
    for routes in maps:
        seeds = np.sort(new_seeds)
        new_seeds = np.copy(seeds)
        print("NEXT ROUTE")
        cont = True
        seedId = np.argmax([seeds >= routes[0].source])
        routeid = bisect_left(routes,seeds[seedId], key=lambda x: x.source) - 1
        #This finds the first routeid that is relevent
        #Now find if that exhausts the seeds or if we need to continue
        while(cont):
            current_route = routes[routeid]
            routeIdEnd = current_route.source + current_route.range_value
            if routeid > -1 and routeIdEnd >= seeds[seedId]:
                #We have found a route appropriate for this seed. We must find out how long it runs for
                if routeIdEnd > seeds[-1]:
                    cont = False
                new_seeds[np.logical_and(current_route.source <= seeds, routeIdEnd > seeds)] += current_route.destination - current_route.source
            if routeid == len(routes)-1:
                cont = False
            if cont:
                seedId = np.argmax([seeds >= routes[routeid+1].source])
                routeid += 1
    return np.min(seeds)
        

def solve_part1(input):
    seeds,maps = parse_input(input)
    return determine_min_location(seeds,maps)

def solve_part2(input):
    seed_parsed,maps = parse_input(input)
    seed_start = seed_parsed[::2]
    seed_range = seed_parsed[1::2]

    min_location = 1e30
    for start,r in zip(seed_start,seed_range):
        seeds = [x for x in range(start,start+r)]
        min_location = min(min_location, determine_min_location(seeds,maps))
    return min_location

if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 1")
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 2")
        print(solve_part2(input))
        