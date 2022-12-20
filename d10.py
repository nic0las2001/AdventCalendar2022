import numpy as np

open_input = open("d10_input.txt","r")

read_input = open_input.read()
instructions = read_input.split('\n')
instructions.remove('')

cycle = 0
register = 1
cyc_dic = {20:False,60:False,100:False,140:False,180:False,220:False,}
cursor = np.array([-1,0,1])+1
drawing = ''

def check_val(cycle,cyc_dic,register):
    if cycle in cyc_dic:
        cyc_dic[cycle] = cycle*register
    return cyc_dic

def draw(cycle,cursor,drawing):
    #print(cycle)
    #print(cursor)
    if (cycle % 40) == 0:
        drawing += '\n'

    if (cycle % 40) in cursor:
        drawing += '#'
    else:
        drawing+='.'

    return drawing

for instruction in instructions:
    data = instruction.split()
    if 'noop' in data:
        drawing = draw(cycle,cursor,drawing)
        cycle += 1
        cyc_dic = check_val(cycle,cyc_dic,register)
    elif 'addx' in data:
        for i in range(2):
            drawing = draw(cycle,cursor,drawing)
            cycle += 1
            cyc_dic = check_val(cycle,cyc_dic,register)
        register += int(data[1])
        cursor += int(data[1])

total_sum = 0
for val in cyc_dic:
    total_sum += cyc_dic[val]

print(total_sum)
print(drawing)
