open_input = open("d6_input.txt","r")

read_input = open_input.read()

#Part 1
for i in range(len(read_input)-4):
    blacklist = []
    for j in range(4):
        if read_input[i+j] not in blacklist:
            blacklist.append(read_input[i+j])
            if len(blacklist) == 4:
                print(i+j+1)
        else:
            break
    if len(blacklist) == 4:
        break

#Part 2
for i in range(len(read_input)-14):
    blacklist = []
    for j in range(14):
        if read_input[i+j] not in blacklist:
            blacklist.append(read_input[i+j])
            if len(blacklist) == 14:
                print(i+j+1)
                break
        else:
            break
    if len(blacklist) == 14:
        break
