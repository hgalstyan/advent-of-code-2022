data = open("input.txt", "r").read().split("\n")

tree = {"/home" : 0}
path = "/home"

def changeDir(dir):
    global path
    
    if dir == "..":
        path = path[:path.rfind("/")]
    elif dir =="/":
        path = "/home"
    else:
        path += "/" + dir
        tree[path] = 0


for line in data:
    if line[0] == "$":
        if line[2:4] == "cd":
            changeDir(line[5:])
    elif line[0:3] != "dir":
        dir = path
        size = int(line.split(" ")[0])
        for i in range(path.count("/")):
            tree[dir] += int(line.split(" ")[0])
            dir = path[:dir.rfind("/")]

total = 0
limit = 30000000 - (70000000 - tree["/home"])
valid_dirs = []

for dir in tree:
    if(tree[dir] <= 100000):
        total += tree[dir]
    if limit <= tree[dir]:
        valid_dirs.append(tree[dir])

print("Answer 1: ", total)
print("Answer 1: ", min(valid_dirs))