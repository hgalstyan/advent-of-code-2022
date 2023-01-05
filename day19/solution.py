import math
import re
import sys
from collections import deque


def solve(blueprint, t):
    raw_costs = list(map(int, re.findall(r"\d+", blueprint)))
    costs = (
        (raw_costs[1], 0, 0, 0),
        (raw_costs[2], 0, 0, 0),
        (raw_costs[3], raw_costs[4], 0, 0),
        (raw_costs[5], 0, raw_costs[6], 0),
    )

    queue = deque()
    queue.append((t, (0, 0, 0, 0), (1, 0, 0, 0)))
    seen = set()
    best = 0
    max_robots = [max(cost[i] for cost in costs) for i in range(4)]

    while queue:
        t, stuff, robots = queue.popleft()
        min_geodes = stuff[3] + t * robots[3]
        if min_geodes > best:
            best = min_geodes

        if (t, stuff, robots) in seen:
            continue
        seen.add((t, stuff, robots))
        if t == 0:
            continue

        # build each thing
        # for each type of robot
        for resource in range(4):

            # check if we have max needed:
            if resource != 3 and robots[resource] >= max_robots[resource]:
                continue

            # make sure have necessary robots
            if any(
                robots[rid] == 0 for rid, cost in enumerate(costs[resource]) if cost
            ):
                continue

            # get wait til until can build robot
            wait = max(
                [
                    math.ceil((cost - stuff[rid]) / robots[rid])
                    for rid, cost in enumerate(costs[resource])
                    if cost
                ]
                + [0]
            )
            if t - wait - 1 <= 0:
                continue

            next_stuff = [
                stuff[i] + (robots[i] * (wait + 1)) - costs[resource][i]
                for i in range(4)
            ]
            next_robots = list(robots)
            next_robots[resource] += 1

            for i in range(3):
                next_stuff[i] = min(next_stuff[i], max_robots[i] * (t - wait - 1))

            queue.append(((t - wait - 1), tuple(next_stuff), tuple(next_robots)))

    return best


data = open("input.txt", "r").readlines()

part1 = 0
for i, line in enumerate(data):
    part1 += (i + 1) * solve(line, 24)
print("Answer 1: ", part1)

part2 = 1
for line in data[:3]:
    part2 *= solve(line, 32)
print("Answer 2: ", part2)
