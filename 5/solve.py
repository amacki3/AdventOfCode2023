import os
import re
from bisect import bisect
import numpy as np


class router:
    def __init__(self, destination: int, source: int, range_value: int):
        self.source = (source)
        self.destination = (destination)
        self.range_value = (range_value)
        # Below for alt part 2
        self.delta = (destination - source)
        self.end = (source + range_value - 1)
        self.start = (source)

    def apply(self, val):
        return val + (self.destination-self.source)


def parse_input(input):
    maps = [[] for i in range(7)]  # 7 is num of maps
    mapIndex = -1
    # we dont have to worry about the routing of the maps, as they are linear and pre-sorted
    for line in input:
        if line.startswith("seeds:"):
            line = line.strip("seeds: ")
            seeds = [int(num) for num in line.split()]
        elif line[0].isdigit():
            nums = line.split()
            maps[int((mapIndex-1)/2)].append(router(int(nums[0]),
                                                    int(nums[1]), int(nums[2])))
            # Could do better with the mapindex, but this works so meh
            print(maps[int((mapIndex-1)/2)][-1].start)
        else:
            mapIndex += 1

        for index, routes in enumerate(maps):
            maps[index] = sorted(routes, key=lambda x: x.source)
    return seeds, maps


def determine_min_location(seeds, maps):
    new_seeds = np.array(seeds)
    # we iterate through our routes and apply them
    # each set of routes is in order now, so we can simply find the first one
    # which has a source above our seed and check if the last ones range fits.
    # We use pyhton built in bisect, which is effectively a binary search alg.
    # For each route we find if any seeds are appropriate and then route it before moving on.
    for routes in maps:
        seeds = np.sort(new_seeds)
        new_seeds = np.copy(seeds)
        print("NEXT ROUTE")
        cont = True
        # This finds the first routeid that is relevent
        # Now find if that exhausts the seeds or if we need to continue
        routeid = bisect(routes, seeds[0], key=lambda x: x.source) - 1
        while (cont):

            current_route = routes[routeid]
            routeIdEnd = current_route.source + current_route.range_value
            if routeIdEnd > seeds[-1]:
                cont = False
            new_seeds[np.logical_and(current_route.source <= seeds, routeIdEnd > seeds)
                      ] += current_route.destination - current_route.source
            if routeid == len(routes)-1:
                cont = False
            if cont:
                routeid += 1

    return np.min(new_seeds)


def solve_part1(input):
    seeds, maps = parse_input(input)
    return determine_min_location(seeds, maps)


def solve_part2(input):
    seed_parsed, maps = parse_input(input)
    seed_start = seed_parsed[::2]
    seed_range = seed_parsed[1::2]

    min_location = 1e30
    for start, r in zip(seed_start, seed_range):
        seeds = [x for x in range(start, start+r)]
        min_location = min(min_location, determine_min_location(seeds, maps))
    return min_location


class seed_range:
    def __init__(self, seed: int, r: int):
        self.start = (seed)
        self.range = (r)
        self.end = (seed + r - 1)


def solve_part2_alt(input):
    seed_parsed, maps = parse_input(input)
    seed_start = seed_parsed[::2]
    seed_range_nums = seed_parsed[1::2]

    seeds = []

    for s, r in zip(seed_start, seed_range_nums):
        seeds.append(seed_range(s, r))
        seeds = sorted(seeds, key=lambda x: x.start)

    # for s in seed_parsed:
    #     seeds.append(seed_range(s,1))

    # preprocessing complete. now lets do it
    for routes in maps:
        new_seeds = []
        print("NEW ROUTE SET")
        # seeds are sorted.
        # routes are sorted
        for sid, seed in enumerate(seeds):
            seed_exhausted = False
            for route in routes:
                if not seed_exhausted:
                    if seed.start <= route.end:
                        if route.start <= seed.end:
                            # The route is in the seed range.
                            # First, deal with any of the seed that exists outside the route range.
                            if seed.start < route.start:
                                # New seed from seed start to route start - 1
                                new_seeds.append(seed_range(
                                    seed.start, route.start - seed.start))

                                # Alter seed to remove this part we have no dealt with...
                                seed = seed_range(
                                    route.start, seed.range - (route.start - seed.start))
                            # Now deal with remaining part within the routes range.
                            if seed.end <= route.end:
                                # careful to use DESTINATION
                                new_start = (
                                    seed.start - route.start) + route.destination
                                new_seeds.append(
                                    seed_range(new_start, seed.range))
                                # seed = seed_range(0, 0)
                                seed_exhausted = True
                            else:
                                new_start = (
                                    seed.start - route.start) + route.destination
                                new_seeds.append(seed_range(
                                    new_start, route.end - seed.start + 1))
                                seed = seed_range(
                                    route.end+1, seed.end - route.end)
            if (not seed_exhausted) and (seed.range > 0):
                new_seeds.append(seed)
        seeds = new_seeds

        sprint = [s.start for s in seeds]

        print(sprint)

    return np.min(sprint)


if __name__ == '__main__':
    # with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
    #     print("Part 1")
    #     print(solve_part1(input))

    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print("Part 2")
        print(solve_part2_alt(input))
