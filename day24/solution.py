from collections import deque
from functools import cache


@cache
def get_storms(t):
    current = set()
    for r, row in enumerate(data[1:-1]):
        for c, char in enumerate(row[1:-1]):
            if char in "<v>^":
                dr, dc = DIRS[char]
                current.add(((r + dr * t) % numr, (c + dc * t) % numc))
    return current


DIRS = {"<": (0, -1), "v": (1, 0), ">": (0, 1), "^": (-1, 0)}

data = open("input.txt", "r").readlines()

numr = len(data) - 2  
numc = len(data[0]) - 3  
start = (-1, data[0].index(".") - 1)
end = (numr, data[-1].index(".") - 1)

queue = deque()
queue.append((0, *start, 0))
seen = set()
part1, part2 = None, None

while not part2:
    t, r, c, leg = queue.popleft()
    if (t, r, c, leg) in seen:
        continue
    seen.add((t, r, c, leg))

    storms = get_storms(t + 1)
    if (r, c) not in storms:
        queue.append((t + 1, r, c, leg))
    for dr, dc in DIRS.values():
        if (r + dr, c + dc) == end and leg in [0, 2]:
            if leg == 0:
                if not part1:
                    part1 = t + 1
                    print("Answer 1: ",part1)
                queue.append((t + 1, r + dr, c + dc, 1))
            else:
                part2 = t + 1
                break
        elif (r + dr, c + dc) == start and leg == 1:
            queue.append((t + 1, *start, 2))
            break
        elif 0 <= r + dr < numr and 0 <= c + dc < numc:
            if (r + dr, c + dc) not in storms:
                queue.append((t + 1, r + dr, c + dc, leg))

print("Answer 2: ",part2)
