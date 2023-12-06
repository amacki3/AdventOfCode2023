import os 
import re
import numpy as np

def solve_for_button(distance,available_time):

    # simple quadratic formula
    distance = distance +1

    discriminant = np.sqrt(available_time*available_time - (4 * distance))

    vals = np.array([available_time - discriminant,available_time + discriminant])/2
    vals[0] = np.ceil(vals[0])
    vals[1] = np.floor(vals[1])
    return vals

def parse_input(input):
    lines = input.readlines()
    times = [int(t) for t in lines[0].split()[1:]]
    distance = [int(d) for d in lines[1].split()[1:]]
    return times, distance


def solve_part1(input):
    total = 1
    times,distance = parse_input(input)
    for t,d in zip(times,distance):
        print(d,t)
        val = solve_for_button(d,t)
        print(val)
        ways = max(val) - min(val) + 1
        print(ways)
        total *= ways
    return total



def solve_part2(input):
    lines = input.readlines()
    total = 1
    times = int(''.join(re.findall('\d',lines[0])))
    distance = int(''.join(re.findall('\d',lines[1])))

    val = solve_for_button(distance,times)
    ways = max(val) - min(val) + 1
    return ways

    

    return 0



if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 1")
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 2")
        print(solve_part2(input))