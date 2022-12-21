open_input = open("d11_input.txt","r")

read_input = open_input.read()

class Monkey:
    def __init__(self,number):
        self.number = number
        self.items = False
        self.operation = False
        self.testval = 0
        self.trueval = -1
        self.falseval = -1
        self.inspected = 0

    def oper(self,item_num,task,modulo):
        relevant = self.operation[23:].split()
        if relevant[1].isnumeric():
            if relevant[0] == '+':
                item_num += int(relevant[1])
            elif relevant[0] == '*':
                item_num *= int(relevant[1])
        else:
            item_num *= item_num

        if task == 1:
            item_num //= 3 #divide and round down to nearest integer
        elif task == 2:
            item_num %= modulo

        return item_num



    def test(self,monkey_list,task,modulo):
        for item in self.items:
            stress_level = self.oper(item,task,modulo)
            self.inspected += 1
            to_send = stress_level

            #print(stress_level)
            if stress_level % self.testval == 0:
                monkey_list[self.trueval].items.append(to_send)
            else:
                monkey_list[self.falseval].items.append(to_send)
        self.items = []

monkey_data = read_input.split('\n\n')

for i in range(len(monkey_data)):
    monkey_data[i] = monkey_data[i].split('\n')


#Initialise the monkeys
monkey_list = []
m_count = 0
task2_modulo = 1
for monkey in monkey_data:
    monkey_list.append(Monkey(m_count))

    for info in monkey:
        if 'Starting' in info:
            starting_items = info[18:]
            starting_items = starting_items.split(', ')
            for i in range(len(starting_items)):
                starting_items[i] = int(starting_items[i])
            #print(starting_items)
            monkey_list[m_count].items = starting_items
        elif 'Operation' in info:
            monkey_list[m_count].operation = info
        elif 'Test' in info:
            monkey_list[m_count].testval = int(info[21:])
        elif 'true' in info:
            monkey_list[m_count].trueval = int(info[29:])
        elif 'false' in info:
            monkey_list[m_count].falseval = int(info[30:])

    task2_modulo *= monkey_list[m_count].testval
    m_count += 1

#Move around the items
#Part 1: 20, Part 2: 10000
task = 2
for i in range(10000):
    for monkey in monkey_list:
        monkey.test(monkey_list,task,task2_modulo)

inspected = []
for monkey in monkey_list:
    inspected.append(monkey.inspected)
    #print(monkey.inspected)

max1 = max(inspected)
inspected.remove(max1)
max2 = max(inspected)

print(max1*max2)


#Part 2
