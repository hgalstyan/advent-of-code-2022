from collections import deque
from functools import cache

data = open("input.txt", "r").readlines()

@cache
def can_get_out(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    seen = set()

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if (x, y, z) in rocks:
            continue
        if x > maxx or x < minx or y > maxy or y < miny or z > maxz or z < minz:
            return True
        for dx, dy, dz in deltas:
            queue.append((x + dx, y + dy, z + dz))
    return False


deltas = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
rocks = set()
for line in data:
    x, y, z = list(map(int, line.split(",")))
    rocks.add((x, y, z))

xs = [x for x, y, z in rocks]
minx, maxx = min(xs), max(xs)
ys = [y for x, y, z in rocks]
miny, maxy = min(ys), max(ys)
zs = [z for x, y, z in rocks]
minz, maxz = min(zs), max(zs)

part1 = 0
part2 = 0
for x, y, z in rocks:
    for dx, dy, dz in deltas:
        if (x + dx, y + dy, z + dz) not in rocks:
            part1 += 1
        if can_get_out(x + dx, y + dy, z + dz):
            part2 += 1

print("Answer 1: ", part1)
print("Answer 2: ", part2)
