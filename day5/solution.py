data = open("test.txt", "r").read().split("\n")
origin, moves = data[:data.index('')], data[data.index('')+1:]
origin = [o.replace("[", "").replace("]", "").replace(" ", "#") for o in origin]
print(origin)
print(moves)

for line in moves:
    _, move, _, _from, _, to = [int(v) if i % 2 else v for i, v in enumerate(line.split())]
    print(move,_from,to)