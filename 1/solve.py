import os
import re

def solve(input,text_tokens=False):

    look_up_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',
    '1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
    total = 0
    digits = [0,0]
    for line in input.split('\n'):
        search_values = "|"
        if text_tokens:
            search_values = "|one|two|three|four|five|six|seven|eight|nine|"
        locs = re.search(search_values[1:] + "\d",line)
        if locs != None:

            digits[0] = line[locs.span()[0]:locs.span()[1]]
            search_values = search_values[::-1]

            locs = re.search(search_values[1:] + "\d",line[::-1])

            digits[1] = line[::-1] [locs.span()[0]:locs.span()[1]] [::-1]

            #Note this works for case where only one number, as start is also end.
            total += int(look_up_dict[digits[0]]+look_up_dict[digits[1]])

    return total



if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        txt = input.read()
        p1 = solve(txt,text_tokens=False)
        p2 = solve(txt,text_tokens=True)
    print("Part 1:")
    print(p1)
    print("Part 2:")
    print(p2)