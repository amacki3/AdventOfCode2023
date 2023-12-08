import os
import re


class fork:
    def __init__(self, name, left, right):
        self.name = name
        self.dir = [left, right]


def parse_input(input):
    lines = input.readlines()
    directions = lines[0].strip()
    f = {}
    first_path = []
    for data in lines[2:]:
        toks = re.findall('([A-Z]+)', data)
        if first_path == []:
            first_path = fork(toks[0], toks[1], toks[2])
        f.update({toks[0]: fork(toks[0], toks[1], toks[2])})
    return directions, f, first_path


def solve_part1(input):
    direc, paths, fp = parse_input(input)
    loc = 'AAA'
    total = 0
    while (not loc == 'ZZZ'):
        loc = paths[loc].dir[int(direc[total % (len(direc))] == 'R')]
        total += 1

    return total


def solve_part2(input):
    return 0


if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part2(input))
