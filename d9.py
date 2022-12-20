import numpy as np

open_input = open("d9_input.txt","r")

read_input = open_input.read()
instructions = read_input.split('\n')
instructions.remove('')

def move(knot, direction):
    base = np.array([0,0])
    mov = {'U':base+[1,0],'D':base+[-1,0],'L':base+[0,-1],'R':base+[0,1]}
    mov['UL'] = mov['U'] + mov['L']
    mov['UR'] = mov['U'] + mov['R']
    mov['DL'] = mov['D'] + mov['L']
    mov['DR'] = mov['D'] + mov['R']

    new_pos = knot + mov[direction]
    return new_pos

H = np.array([0,0])
T = np.array([0,0])
T_history = [[0,0]]

catchup = {-2:-1,2:1}
small_catchup = {-1:-1,1:1}

for instruction in instructions:
    data = instruction.split()
    for disp in range(int(data[1])):
        H = move(H,data[0])
        #print(H,T)
        delta = H-T
        if delta[0] in catchup:
            T[0] += catchup[delta[0]]
            if delta[1] in small_catchup:
                T[1] += small_catchup[delta[1]]
        if delta[1] in catchup:
            T[1] += catchup[delta[1]]
            if delta[0] in small_catchup:
                T[0] += small_catchup[delta[0]]
        if list(T) not in T_history:
            T_history.append(list(T))

#print(T_history)
print('Part 1: ',len(T_history))

#Part 2
knots = []
for i in range(10):
    knots.append(np.array([0,0]))
T_history = [[0,0]]

catchup = {-2:-1,2:1}
small_catchup = {-1:-1,1:1}

for instruction in instructions:
    data = instruction.split()
    for disp in range(int(data[1])):
        knots[0] = move(knots[0],data[0])
        for i in range(9):
            delta = knots[i]-knots[i+1]
            if delta[0] in catchup:
                knots[i+1][0] += catchup[delta[0]]
                if delta[1] in small_catchup:
                    knots[i+1][1] += small_catchup[delta[1]]
            if delta[1] in catchup:
                knots[i+1][1] += catchup[delta[1]]
                if delta[0] in small_catchup:
                    knots[i+1][0] += small_catchup[delta[0]]
            if list(knots[9]) not in T_history:
                T_history.append(list(knots[9]))

print('Part 2: ',len(T_history))
