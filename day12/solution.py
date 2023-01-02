from collections import defaultdict, deque

data = open("input.txt", "r").read().split("\n")


def init(data, is_part2):
    _map = []
    for i in range(len(data)):
        line = list(data[i])
        if "S" in line:
            sx = line.index("S")
            line[sx] = "a"
        if "E" in line:
            ex = line.index("E")
            target = (i, ex)
            line[ex] = "z"
        if(is_part2):     
            for idx in range(len(line)):
                if line[idx] == "a":
                    starts.append((i, idx))
        _map.append([ord(i) for i in line])
    return _map


_map = init(data, False)
start = None
target = None

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([(start, 0)])
seen = defaultdict(int)
seen[start] = 0

res = 0

while queue:
    pos, step = queue.popleft()

    if pos == target:
        res = step

    next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in d]
    for np in next_pos:
        if not 0 <= np[0] < len(_map) or not 0 <= np[1] < len(_map[0]):
            continue
        if np in seen and seen[np] <= step + 1:
            continue
        if _map[np[0]][np[1]] - _map[pos[0]][pos[1]] > 1:
            continue

        seen[np] = step + 1
        queue.append((np, step + 1))

print("Answer 1: ", res)

_map = init(data, True)
starts = []
target = None
res = 99999
queue = deque([(target, 0)])
seen = defaultdict(int)
seen[target] = 0

while queue:
    pos, step = queue.popleft()

    if pos in starts:
        if step < res:
            res = step
        continue

    if step > res:
        continue

    next_pos = [(pos[0] + dy, pos[1] + dx) for dy, dx in d]
    for np in next_pos:
        if not 0 <= np[0] < len(_map) or not 0 <= np[1] < len(_map[0]):
            continue
        if np in seen and seen[np] <= step + 1:
            continue
        if _map[np[0]][np[1]] - _map[pos[0]][pos[1]] < -1:  # from target to start, we need to go down
            continue

        seen[np] = step + 1
        queue.append((np, step + 1))

print("Answer 2: ", res)
