open_input = open("d2_input.txt","r")

read_input = open_input.read()
games = read_input.split('\n')
choices = []

for game in games:
    choices.append(game.split(' '))

tie = [['A','X'],['B', 'Y'],['C', 'Z']]
win = [['C','X'],['A', 'Y'],['B', 'Z']]
loss = [['A','Z'],['B', 'X'],['C', 'Y']]

bonus = {'X':1,'Y':2,'Z':3}

total_score = 0
for choice in choices:
    if choice in tie:
        total_score += 3
    elif choice in win:
        total_score += 6
    else:
        total_score += 0
    if len(choice) > 1:
        total_score += bonus[choice[1]]

print(total_score)

#PART 2
#X - lose, Y - Win, Z - draw
win_status = {'X':0,'Y':3,'Z':6}
status_combo = {'X':loss,'Y':tie,'Z':win}
total_score = 0
for choice in choices:
    if len(choice)>1:
        total_score += win_status[choice[1]]
        match = status_combo[choice[1]]
        for item in match:
            if choice[0] in item:
                total_score += bonus[item[1]]

print(total_score)
