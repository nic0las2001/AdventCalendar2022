import numpy as np

open_input = open("d8_input.txt","r")

read_input = open_input.read()

lines = read_input.split('\n')

array = []
for line in lines:
    line_list = []
    for char in line:
        if char.isnumeric():
            line_list.append(int(char))
    if len(line_list) > 0:
        array.append(line_list)

count = 0
matrix = np.array(array)
dim = [0,matrix.shape[1]-1]

#Part 1
for i in range(matrix.shape[1]):
    for j in range(matrix.shape[1]):
        #Border case
        if i in dim or j in dim:
            count += 1
        else:
            #Horizontal case
            if np.max(matrix[i,:j]) < matrix[i,j] or np.max(matrix[i,j+1:]) < matrix[i,j]:
                count +=1
            #Vertical case
            elif np.max(matrix[:i,j]) < matrix[i,j] or np.max(matrix[i+1:,j]) < matrix[i,j]:
                count +=1

print(count)

max_score = 0
#Part 2
for i in range(matrix.shape[1]):
    for j in range(matrix.shape[1]):
        #Border case
        #print(matrix[i,j])
        if i in dim or j in dim:
            score = 0
        else:
            #Up case
            up = 1
            while matrix[i,j] > matrix[i-up,j]:
                if i - up == 0:
                    break
                up += 1
            #Down case
            down = 1
            while matrix[i,j] > matrix[i+down,j]:
                if i + down == dim[1]:
                    break
                down += 1
            #Left case
            left = 1
            while matrix[i,j] > matrix[i,j-left]:
                if j - left == 0:
                    break
                left += 1
            #Right case
            right = 1
            while matrix[i,j] > matrix[i,right+j]:
                if j + right == dim[1]:
                    break
                right += 1
            score = up*down*left*right
            if score > max_score:
                max_score = score

print(max_score)
