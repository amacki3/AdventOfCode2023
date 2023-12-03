import os
import re

def solve_part1(input):
    total = 0
    for line in input.split('\n'):
        print(line)
        digits = re.findall('\d',line)
        if (len(digits) < 1):
            digits = ['0']
        #Note this works for case where only one number, as start is also end.
        total += int(digits[0]+digits[-1])

    return total

def solve_part2(input):
    #Use part 1 solver, but first massage input
    #order . e.g. eightwo needs to be eight, but twoneight needs to be two etc.
    num_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for k,v in num_dict.items():
        input = input.replace(k,v)
    return solve_part1(input)


if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        txt = input.read()
        p1 = solve_part1(txt)
        p2 = solve_part2(txt)
    print("Part 1:")
    print(p1)
    print("Part 2:")
    print(p2)