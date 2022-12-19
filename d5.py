import pandas as pd
import copy
open_input = open("d5_input.txt","r")

read_input = open_input.read()
input = read_input.split('\nmove')

layout = input[0].split('\n')
del layout[len(layout)-1]

#Read through the piles
headers = list(range(1,10))
piles = {}
for item in headers:
    piles[item] = []
columns = []
blacklist = [' ','[',']']
#[columns.append(layout[i].split(' ','[',']')) for i in range(len(layout)-1)]
for item in layout:
    i = 0
    for char in item:
        if char.isalpha():
            key = (i-1)/4+1
            piles[key].append(char)
        i += 1

for key in piles:
    piles[key].reverse()

del input[0]

instructions = []
for instruction in input:
    s = []
    for char in instruction.split():
        try:
            s.append(int(char))
        except:
            pass
    instructions.append(s)

piles2 = copy.deepcopy(piles)
piles1 = copy.deepcopy(piles)

def move_crate(number,origin,destination,piles):
    for crate in range(number):
        piles[destination].append(piles[origin].pop(-1))
    return piles

def move_crate2(number,origin,destination,piles2):
    for crate in range(number,0,-1):
        piles2[destination].append(piles2[origin].pop(-crate))
    return piles2

for ins in instructions:
    piles1 = move_crate(ins[0],ins[1],ins[2],piles1)
    piles2 = move_crate2(ins[0],ins[1],ins[2],piles2)

final_string = ''
final_string2 = ''
for key in piles:
    final_string+=piles1[key][-1]
    final_string2+=piles2[key][-1]
print(final_string)
print(final_string2)

#print(layout)
