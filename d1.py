open_input = open("d1_input.txt","r")

read_input = open_input.read()
input_list = read_input.split('\n\n')
#print(input_list)

sum_list = []
for item in input_list:
    numeric_input = []
    split_item = item.split('\n')
    for subitem in split_item:
        if subitem.isnumeric():
            numeric_input.append(int(subitem))
    sum_list.append(sum(numeric_input))

print(max(sum_list)) #Elf carrying max amount of calories (Q1)

count = max(sum_list)
for i in range(2):
    sum_list.remove(max(sum_list))
    count += max(sum_list)

print(count)
