open_input = open("d7_input.txt","r")

read_input = open_input.read()

class directory:
    def __init__(self,name,uuid):
        self.name = name
        self.subdirectories = []
        self.files = []
        self.outer = 0 #uuid
        self.dir_size = 0
        self.uuid = uuid

    def add_subdir(self,subdir_uuid):
        self.subdirectories.append(subdir_uuid)

    def add_file(self,file):
        size = ''
        for char in file:
            if char.isnumeric():
                size += char
            else:
                break
        self.files.append(int(size))

    def find_dir_size(self,directories):
        dir_size = sum(self.files)
        for subdir in self.subdirectories:
            #print(subdir)
            #if directories[subdir].dir_size == False:
            dir_size += directories[subdir].find_dir_size(directories)

        self.dir_size = dir_size
        return dir_size

commands = read_input.split('\n')
try:
    commands.remove('')
except:
    pass

def finduuid(name, directories, outer):
    for uuid in directories:
        if directories[uuid].name == name and directories[uuid].outer == outer:
            return uuid

directories = {}
uuid = 0

current_dir = ''
current_dir_uuid = 0
for command in commands:
    if '$ cd' in command: #Directory management
        if '..' in command: #Go up one
            #print(current_dir)
            current_dir_uuid = directories[current_dir_uuid].outer
        else: #Create new directory
            current_dir = command[5:]
            current_dir_uuid = finduuid(current_dir, directories, current_dir_uuid)
            if current_dir_uuid not in directories:
                directories[uuid] = directory(current_dir,uuid)
                current_dir_uuid = uuid
                uuid += 1
    elif '$ ls' in command:
        pass
    elif 'dir' in command:
        #name: command[4:]
        directories[current_dir_uuid].add_subdir(uuid)
        directories[uuid] = directory(command[4:],uuid)
        directories[uuid].outer = current_dir_uuid
        uuid += 1
    elif command[0].isnumeric():
        directories[current_dir_uuid].add_file(command)

total_sum = 0
min = 1e15
total_used = directories[0].find_dir_size(directories)
delta = - 7e7 + total_used + 3e7
for item in directories:
    if item != -1:
        size = directories[item].find_dir_size(directories)
        if size <= 100000:
            total_sum += size

        #Part 2
        if size >= delta and size < min:
            min = size

print("Part 1: ",total_sum)
print("Part 2\nTotal used: ", directories[0].dir_size)
print('Wanted value: ', min)
