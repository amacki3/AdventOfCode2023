import os 
import re
from bisect import bisect
import numpy as np

class router:
    def __init__(self,destination,source,range_value):
        self.source = np.int64(source)
        self.destination = np.int64(destination)
        self.range_value = np.int64(range_value)
        #Below for alt part 2
        self.delta = np.int64(destination - source)
        self.end = np.int64(source + range_value - 1)
        self.start = np.int64(source)
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
        #This finds the first routeid that is relevent
        #Now find if that exhausts the seeds or if we need to continue 
        routeid = bisect(routes,seeds[0], key=lambda x: x.source) - 1
        while(cont):

            current_route = routes[routeid]
            routeIdEnd = current_route.source + current_route.range_value
            if routeIdEnd > seeds[-1]:
                cont = False
            new_seeds[np.logical_and(current_route.source <= seeds, routeIdEnd > seeds)] += current_route.destination - current_route.source
            if routeid == len(routes)-1:
                cont = False
            if cont:
                routeid += 1
    
    return np.min(new_seeds)
        

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


class seed_range:
    def __init__(self,seed,r):
        self.start = np.int64(seed)
        self.range = np.int64(r)
        self.end = np.int64(seed + r - 1)

def solve_part2_alt(input):
    seed_parsed,maps = parse_input(input)
    seed_start = seed_parsed[::2]
    seed_range_nums = seed_parsed[1::2]

    seeds = []

    for s,r in zip(seed_start,seed_range_nums):
        seeds.append(seed_range(s,r))
        seeds= sorted(seeds,key=lambda x: x.start)

    # for s in seed_parsed:
    #     seeds.append(seed_range(s,1))

    #preprocessing complete. now lets do it
    for routes in maps:
        new_seeds = []
        print("NEW ROUTE SET")
        routeid = 0
        #seeds are sorted.
        #routes are sorted
        for seed in seeds:
            routeid = 0
            #find the first route that is appropriate and work forward
            found = False
            while(routeid < len(routes) and not found):
                if seed.start > routes[routeid].end:
                    routeid += 1
                else:
                    if seed.end <= routes[routeid].end:
                        if seed.start >= routes[routeid].start:
                            #Simple, route encompasses seed. add new seed all changed
                            new_seeds.append(seed_range(seed.start + routes[routeid].delta,seed.range))
                            found = True
                        else:
                            #Seed start is earlier, so find what needs to happen and we have exhausted this seed.
                            if seed.end < routes[routeid].start:
                                new_seeds.append(seed)
                                found = True
                            else:
                                left_range = routes[routeid].start - seed.start
                                if left_range >= 0:
                                    new_seeds.append(seed_range(seed.start,left_range))
                                right_range = seed.range - left_range
                                if right_range >= 0:
                                    new_seeds.append(seed_range(routes[routeid].destination,right_range))
                                found = True
                    else:
                        #Route is not fully encompassing, work it out.
                        if seed.start < routes[routeid].start:
                            left_range = routes[routeid].start - seed.start
                            new_seeds.append(seed_range(seed.start,left_range))
                            #We now know that the right_range is wider than the route, so we add a seed the length of the route
                            new_seeds.append(seed_range(routes[routeid].destination,routes[routeid].range_value))
                            #And we have the remaining part of the seed
                            seed = seed_range(routes[routeid].end+1,seed.end - routes[routeid].end)
                        else:
                            #Seed is longer than the route but starts in it
                            left_range = routes[routeid].end - seed.start
                            new_seeds.append(seed_range(seed.start,left_range))
                            seed = seed_range(routes[routeid].end+1,seed.range-left_range)

                    routeid += 1
            if not found:
                new_seeds.append(seed)
        seeds = sorted(new_seeds,key = lambda x: x.start)
        # seeds = [s for s in seeds if not s.start == 0]
        sprint = [s.start for s in seeds]
        print("SEEDS:", sprint)

    return seeds[0].start

if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 1")
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 2")
        print(solve_part2_alt(input))
        