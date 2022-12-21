import numpy as np
import string

#See: Dijkstra's algorithm

open_input = open("d12_input.txt","r")

read_input = open_input.read()
lines = read_input.split('\n')
lines.remove('')

height_dict = {}
for char in string.ascii_lowercase:
    height_dict[char] = string.ascii_lowercase.index(char)
height_dict['S'] = 'S'
height_dict['E'] = 'E'

table = []
for line in lines:
    new_line = []
    for char in line:
        new_line.append(height_dict[char])
    table.append(new_line)

array = np.array(table)
start = (np.where(array == 'S')[0][0],np.where(array == 'S')[1][0])
end = (np.where(array == 'E')[0][0],np.where(array == 'E')[1][0])

distances = {}

for j in range(len(new_line)):
    for i in range(len(table)):
        if (i,j) != end: #change start/end for part 2
            distances[(i,j)] = np.inf

unvisited = list(distances.keys())
visited = []
current_coord = end

def dist_update(i,j,distances,next):
    if distances[next] == np.inf:
        distances[next] = distances[(i,j)] + 1
        return distances
    elif distances[next] > distances[(i,j)]:
        distances[next] = distances[(i,j)] + 1
        return distances
    else:
        return distances

def findPath(i,j,array,distances,visited):
    #print(array)
    flag = False
    if str(array[i,j]).isnumeric() == False:
        if array[i,j] == 'E':
            array[i,j] = 25
        '''if array[i,j] == 'S':
            array[i,j] = 0'''
    #Down
    if flag:
        pass
    else:
        if i < array.shape[0]-1 and (i+1,j) not in visited: #40
            #print(array[i+1,j],array[i,j])
            if array[i+1,j] == 'E':
               num = 25
            elif array[i+1,j] == 'S':
                  num = 0
            else:
               num = int(array[i+1,j])

            if num - int(array[i,j]) >= -1: # <= 1: #change for part 1/2
                distances = dist_update(i,j,distances,(i+1,j))
        #Up
        if i > 0 and (i-1,j) not in visited:
            if array[i-1,j] == 'E':
                num = 25
            elif array[i-1,j] == 'S':
                  num = 0
            else:
                num = int(array[i-1,j])
            if num - int(array[i,j]) >= -1: # <= 1:
                distances = dist_update(i,j,distances,(i-1,j))
        #Right
        if j < array.shape[1]-1 and (i,j+1) not in visited: #179
            if array[i,j+1] == 'E':
                num = 25
            elif array[i,j+1] == 'S':
                  num = 0
            else:
                num = int(array[i,j+1])
            if num - int(array[i,j]) >= -1: # <= 1:
                distances = dist_update(i,j,distances,(i,j+1))

        #Left
        if j > 0 and (i,j-1) not in visited:
            if array[i,j-1] == 'E':
                num = 25
            elif array[i,j-1] == 'S':
                  num = 0
            else:
                num = int(array[i,j-1])
            if num - int(array[i,j]) >= -1: # <= 1:
                distances = dist_update(i,j,distances,(i,j-1))
        visited.append((i,j))
    return distances, visited

steps = 0
(i,j) = current_coord
distances[(i,j)] = 0

#Part 2
current_coord  = end
a_coords = []

for key, val in distances.items():
    (p,q) = key
    if array[p,q] == '0':
        a_coords.append((p,q))

while a_coords not in visited: #change start/end part 2
    (i,j) = current_coord
    distances, visited = findPath(i,j,array,distances,visited)
    if current_coord in unvisited:
        unvisited.remove(current_coord)
    unvisited_dic = {}
    for key, val in distances.items():
        if key in unvisited:
            unvisited_dic[key] = val
    print(len(visited)/(array.shape[0]*array.shape[1]))
    if len(unvisited_dic) > 0:
        current_coord = min(unvisited_dic, key=unvisited_dic.get)

print(distances[end])
