import os
import re
import numpy as np


def solve(input):
    total = 0
    for line in input:
        line_total = 0
        winning_str = line.split('|')[0]
        to_check_str = line.split('|')[1]

        winning_str_start = winning_str.find(':')

        winning_str = re.finditer(
            ('\w(\d*)'), winning_str[winning_str_start+1:])
        to_check_str = re.finditer(('\w(\d*)'), to_check_str[1:])

        winning_nums = []

        for winners in winning_str:  # and our nums
            winning_nums.append(int(winners.group(0)))
        for nums in to_check_str:
            if int(nums.group(0)) in winning_nums:
                if line_total == 0:
                    line_total = 1
                else:
                    line_total *= 2
        total += line_total

    return total


def solve_part2(input):

    lines = input.readlines()
    numCards = len(lines)
    num_evals = [1 for i in range(numCards)]
    for id, line in enumerate(lines):
        line_total = 0
        winning_str = line.split('|')[0]
        to_check_str = line.split('|')[1]

        winning_str_start = winning_str.find(':')

        winning_str = re.finditer(
            ('\w(\d*)'), winning_str[winning_str_start+1:])
        to_check_str = re.finditer(('\w(\d*)'), to_check_str[1:])

        winning_nums = []
        for winners in winning_str:  # and our nums
            winning_nums.append(int(winners.group(0)))
        for nums in to_check_str:
            if int(nums.group(0)) in winning_nums:
                line_total += 1
                num_evals[id+line_total] += (num_evals[id])

    return np.sum(np.array(num_evals))


if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part2(input))
