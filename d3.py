import string

open_input = open("d3_input.txt","r")

read_input = open_input.read()
bags = read_input.split("\n")

#Part 1
letter_list = []
for bag in bags:
    for letter in bag[:int(len(bag)/2)]:
        if letter in bag[int(len(bag)/2):]:
            letter_list.append(letter)
            break

#Part 2
letter_list2 = []
i = 0
for i in range(len(bags)):
    if i % 3 == 0:
        for letter in bags[i]:
            if letter in bags[i+1] and letter in bags[i+2]:
                letter_list2.append(letter)
                break
    i += 1

def score_count(letter_list):
    count = 0
    for letter in letter_list:
        if letter.islower():
            val = 1+string.ascii_lowercase.index(letter)
        else:
            val = 27+string.ascii_lowercase.index(letter.lower())
        count += val
    return count

print(score_count(letter_list))
print(score_count(letter_list2))
