import os
import re
import numpy as np

def solve(input):
    total = 0
    for id,line in enumerate(input):
        blue = np.array(re.findall('(\d*) blue', line),dtype=int)
        red = np.array(re.findall('(\d*) red', line),dtype=int)
        green = np.array(re.findall('(\d*) green', line),dtype=int)
        if not(any(blue > 14) or any(red > 12) or any( green > 13)):
            total += id+1
           
        
    return total


if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print(solve(input))
        