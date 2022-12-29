data = open("input.txt", "r").read().split("\n")

sep = [i for i, v in enumerate(data) if v == ""][0]

crates = data[: sep - 1][::-1]
procedures = data[sep + 1 :]

stack_num = max(map(int, data[sep - 1].split()))
stacks1 = [[] for _ in range(stack_num + 1)]
stacks2 = [[] for _ in range(stack_num + 1)]

for line in crates:
    items = [line[i] for i in range(1, len(line), 4)]
    for i, v in enumerate(items):
        if v != " ":
            stacks1[i + 1].append(v)
            stacks2[i + 1].append(v)


for line in procedures:
    _, move, _, _from, _, to = [int(v) if i % 2 else v for i, v in enumerate(line.split())]
    
    moving_crates1 = stacks1[_from][-move:]
    moving_crates1 = moving_crates1[::-1]
    stacks1[to].extend(moving_crates1)
    del stacks1[_from][-move:]

    moving_crates2 = stacks2[_from][-move:]
    stacks2[to].extend(moving_crates2)
    del stacks2[_from][-move:]

print("Answer 1: ", "".join(stacks1[i][-1] for i in range(1, len(stacks1))))
print("Answer 2: ", "".join(stacks2[i][-1] for i in range(1, len(stacks2))))