data = open("input.txt", "r").read().split("\n")


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


sensors = []
beacons = []
for line in data:
    parts = line.split(" ")

    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])

    sensors.append((sx, sy))
    beacons.append((bx, by))


dists = []

for i in range(len(sensors)):
    dists.append(dist(sensors[i], beacons[i]))

Y = 2000000

intervals = []

for i, s in enumerate(sensors):
    dx = dists[i] - abs(s[1] - Y)

    if dx <= 0:
        continue

    intervals.append((s[0] - dx, s[0] + dx))


# INTERVAL OVERLAP ETC.
allowed_x = []
for bx, by in beacons:
    if by == Y:
        allowed_x.append(bx)

min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

ans = 0
for x in range(min_x, max_x + 1):
    if x in allowed_x:
        continue

    for left, right in intervals:
        if left <= x <= right:
            ans += 1
            break

print("Answer 1: ", ans)


pos_lines = []
neg_lines = []

for i, s in enumerate(sensors):
    d = dists[i]
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])


pos = None
neg = None

for i in range(2 * len(sensors)):
    for j in range(i + 1, 2 * len(sensors)):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1


x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4000000 + y

print("Answer 2: ", ans)
