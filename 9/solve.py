import numpy as np
import os



def solve_part1(input):
    total = 0
    for line in input:
        data = [np.array([int(x) for x in line.split()])]
        complete = False
        while not complete:
            data.append(np.diff(data[-1])) 
            if len(np.unique(data[-1])) == 1:
                complete = True
        for id in range(len(data)-1,0,-1):
            data[id-1][-1] += data[id][-1]
        total += data[0][-1]


    return total

def solve_part2(input):
    total = 0
    for line in input:
        data = [np.array([int(x) for x in line.split()])]
        complete = False
        while not complete:
            data.append(np.diff(data[-1])) 
            if len(np.unique(data[-1])) == 1:
                complete = True
        for id in range(len(data)-1,0,-1):
            data[id-1][0] -= data[id][0]
        total += data[0][0]
    return total








if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part2(input))