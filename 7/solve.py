import os 
import re
import numpy as np


def base13_int(string_value):
    card_dict = {'A':0xe,'K':0xd,'Q':0xc,'J':0xb,'T':0xa,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return card_dict[string_value]

def base13_int_mod(string_value):
    card_dict = {'A':0xe,'K':0xd,'Q':0xc,'J':0,'T':0xa,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return card_dict[string_value]

def solve_part1(input):
    lines = input.readlines()
    
    rank_value = np.zeros(len(lines))
    bid_values = np.zeros(len(lines))

    for index,data in enumerate(lines):
        bid_values[index] = int(data.split()[1])
        cards = data.split()[0]
        #we assign a value based on the base 14 value of the 5 entries
        for pos,char in enumerate(cards):
            rank_value[index] += (15**(len(cards) - pos)) * base13_int(char)
        
        #Now we determine the actual value of the hand
        #First determine the base value of it all
        #We take the number of distinct cards and this gives us a rough ordering -> less cards the higher you are
        #But there are cases where this is not always good, so we also need to know longest run. Longest run is best.
        #7 total hands, which means we can mult by 2 and stay in our bound of 15.
        uVal,count = np.unique([x for x in cards],return_counts=True)
        posVal = len(cards) - len(uVal)
        seperator = (posVal == 2) * (np.max(count) == 3) + (posVal == 3) * (np.max(count) == 4)

        rank_value[index] +=  (posVal*2 + seperator) * (15 ** (len(cards) +1 ) )
    bid_values = bid_values[np.argsort(rank_value)]

    return np.sum(np.array(bid_values) * np.arange(1,len(bid_values) +1)) 

def solve_part2(input):
    lines = input.readlines()
    
    rank_value = np.zeros(len(lines))
    bid_values = np.zeros(len(lines))

    for index,data in enumerate(lines):
        bid_values[index] = int(data.split()[1])
        cards = data.split()[0]
        #we assign a value based on the base 14 value of the 5 entries
        for pos,char in enumerate(cards):
            rank_value[index] += (15**(len(cards) - pos)) * base13_int_mod(char)
        

        #Now we determine the actual value of the hand
        #First determine the base value of it all
        #We take the number of distinct cards and this gives us a rough ordering -> less cards the higher you are
        #But there are cases where this is not always good, so we also need to know longest run. Longest run is best.
        #7 total hands, which means we can mult by 2 and stay in our bound of 15.
        uVal,count = np.unique([x for x in cards if not x == 'J'],return_counts=True)
        #determine replacement
        if len(uVal) > 0:
            rep_letter = uVal[np.argmax(count)]
        else:
            rep_letter = '0'
        cards = cards.replace('J',rep_letter)

        uVal,count = np.unique([x for x in cards],return_counts=True)
        posVal = len(cards) - len(uVal)
        seperator = (posVal == 2) * (np.max(count) == 3) + (posVal == 3) * (np.max(count) == 4)

        rank_value[index] +=  (posVal*2 + seperator) * (15 ** (len(cards) +1 ) )
    bid_values = bid_values[np.argsort(rank_value)]

    return np.sum(np.array(bid_values) * np.arange(1,len(bid_values) +1)) 

if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 1")
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print("Part 2")
        print(solve_part2(input))