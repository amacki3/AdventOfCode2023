import os 
import re

def check_token(tok):
    if tok not in ['.','0','1','2','3','4','5','6','7','8','9','\n']:
        print(tok)
        return False
    return True

def solve(input):

    lines = input.readlines()
    total = 0
    maxLines = len(lines)

    for id,data in enumerate(lines):

        toks = re.finditer('(\d*)',data)


        for matches in toks:
            span = matches.span()
            found = False
            for loc in range(span[0],span[1]):
                if not found and not loc == 0:
                    #Check to the left of the string, and above and below it
                    if not (check_token(data[loc-1])):
                        found = True 
                    elif not(id == 0) and not (check_token(lines[id-1][loc-1])):
                        found = True
                    elif not(id + 1 == maxLines) and not (check_token(lines[id+1][loc-1])):
                        found = True

                    #Now check above and below it
                    elif not(id == 0) and not (check_token(lines[id-1][loc])):
                        found = True
                    elif not(id + 1 == maxLines) and not (check_token(lines[id+1][loc])):
                        found = True

                    #And now to the right and above it. This will duplicate checks, but oh well, elegance to the window
                   
                    elif not(loc+1 == len(data)):
                        if not (check_token(data[loc+1])):
                            found = True 
                        elif not(id == 0) and not (check_token(lines[id-1][loc+1])):
                            found = True
                        elif not(id + 1 == maxLines) and not (check_token(lines[id+1][loc+1])):
                            found = True
                if found:
                    break
            if found:
                num = int(matches.group(0))
                total += num

    return total

                    
                    

if __name__ == '__main__':
    with open('/'.join([os.path.dirname(os.path.abspath(__file__)),'input.txt'])) as input:
        print(solve(input))
