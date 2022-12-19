open_input = open("d4_input.txt","r")

read_input = open_input.read()

pairs = read_input.split('\n')
if len(pairs[len(pairs)-1]) < 2:
    del pairs[len(pairs)-1]

num_list = []
for pair in pairs:
    pair_clean = pair.split(',')
    for numbers in pair_clean:
        num = numbers.split('-')
        num_list.append([int(num[0]),int(num[1])])

#print(num_list)

i = 0
count = 0
count2 = 0
for i in range(len(num_list)):
    if i % 2 == 0:
        a = list(range(num_list[i][0],(num_list[i][1])+1))
        b = list(range(num_list[i+1][0],(num_list[i+1][1]+1)))
        if set(a) & set(b):
            c = set(a) & set(b)
            count2 += 1
            if set(a) == c or set(b) == c:
                count +=1

print(count, count2)
