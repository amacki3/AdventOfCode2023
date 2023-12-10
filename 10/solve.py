import numpy as np
import os


move_dict = {'|':[[1,0],[-1,0]],'L':[[0,1],[-1,0]],'F':[[0,1],[1,0]],'J':[[-1,0],[0,-1]],'7':[[1,0],[0,-1]],'-':[[0,1],[0,-1]]}
inside_loop = {'|':[[0,1],[0,-1]}


def parse_input(input):
    data = input.readlines()
    return data

def find_start_positions(data):
    y = 0
    x = 0
    for id,line in enumerate(data):
        if 'S' in line:
            x = line.index('S')
            y = id
    return (x,y)

def get_starting_nodes(start_pos,data):
    nodes = [[0,0],[0,0]]
    node_1_found = False
    if data[start_pos[0]-1][start_pos[1]] in ['|','F','7']:
        nodes[0] = [start_pos[0]-1,start_pos[1]]
        node_1_found = True
    if data[start_pos[0]+1][start_pos[1]] in ['|','J','L']:
        if node_1_found:
            nodes[1] = [start_pos[0]+1,start_pos[1]]
            return nodes
        else:
            nodes[0] = [start_pos[0]+1,start_pos[1]]
            node_1_found = True
    if data[start_pos[0]][start_pos[1]+1] in ['-','J','7']:
        if node_1_found:
            nodes[1] = [start_pos[0],start_pos[1]+1]
            return nodes
        else:
            nodes[0] = [start_pos[0],start_pos[1]+1]
            node_1_found = True
    
    if data[start_pos[0]][start_pos[1]-1] in ['-','L','F']:
        nodes[1] = [start_pos[0],start_pos[1]-1]
        return nodes

def solve_part1(input):
    total = 1
    data = parse_input(input)
    #Get where we are starting    
    start_x,start_y = find_start_positions(data)
    nodes = [[0,0],[0,0]] #maintain where we are
    last_nodes = [[start_y,start_x],[start_y,start_x ]] #and where we have been
    
    #find both nodes that work
    nodes = get_starting_nodes([start_y,start_x],data)
    #Now loop to solve
    notFound = True
    while notFound:
        total += 1
        new_node = [[0,0],[0,0]]
        for x in range(2):
            new_node[x][0] = move_dict[data[nodes[x][0]][nodes[x][1]]][0][0] + nodes[x][0]
            new_node[x][1] = move_dict[data[nodes[x][0]][nodes[x][1]]][0][1] + nodes[x][1]
            if new_node[x] == last_nodes[x]:
                new_node[x][0] = move_dict[data[nodes[x][0]][nodes[x][1]]][1][0] + nodes[x][0]
                new_node[x][1] = move_dict[data[nodes[x][0]][nodes[x][1]]][1][1] + nodes[x][1]

        last_nodes[0] = nodes[0]
        last_nodes[1] = nodes[1]
        nodes[0] = new_node[0]
        nodes[1] = new_node[1]

        if nodes[0] == nodes[1]:
            #Found the loc, stop
            notFound = False
        elif nodes[0] == last_nodes[1] and nodes[1] == last_nodes[0]:
            #Also found, as we have passed each other
            notFound = False
            total -= 1

    return total

def solve_part2(input):
    #Copy Paste part 1
    total = 1
    data = parse_input(input)
    #Get where we are starting    
    start_x,start_y = find_start_positions(data)
    nodes = [[0,0],[0,0]] #maintain where we are
    last_nodes = [[start_y,start_x],[start_y,start_x ]] #and where we have been
    
    #find both nodes that work
    nodes = get_starting_nodes([start_y,start_x],data)
    #Now loop to solve
    notFound = True
    while notFound:
        total += 1
        new_node = [[0,0],[0,0]]
        for x in range(2):
            new_node[x][0] = move_dict[data[nodes[x][0]][nodes[x][1]]][0][0] + nodes[x][0]
            new_node[x][1] = move_dict[data[nodes[x][0]][nodes[x][1]]][0][1] + nodes[x][1]
            if new_node[x] == last_nodes[x]:
                new_node[x][0] = move_dict[data[nodes[x][0]][nodes[x][1]]][1][0] + nodes[x][0]
                new_node[x][1] = move_dict[data[nodes[x][0]][nodes[x][1]]][1][1] + nodes[x][1]

        last_nodes[0] = nodes[0]
        last_nodes[1] = nodes[1]
        nodes[0] = new_node[0]
        nodes[1] = new_node[1]
        #Now for the part 2 attempt. We select a direction ('left or right' of our first node and colour all the data to that side with a number if its a '.' we can then add these up at the end as 'inside')


    return total








if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part1(input))
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])) as input:
        print(solve_part2(input))