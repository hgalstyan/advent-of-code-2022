from functools import cache

data = open("input.txt", "r").read().split("\n")

flows = {}
maps = {}
for line in data:
    toksen = line.split(" ")
    valve = toksen[1]
    flows[valve] = int(toksen[4].split("=")[1].strip(";"))
    maps[valve] = [t.strip(",\n") for t in toksen[9:]]

@cache
def solve(pos, time, opened, ele_wait=False):
    if time == 0:
        if ele_wait:
            return solve("AA", 26, opened)
        return 0

    score = max(solve(n, time - 1, opened, ele_wait) for n in maps[pos])

    if flows[pos] > 0 and pos not in opened:
        new_opened = set(opened)
        new_opened.add(pos)
        score = max(score, (time - 1) * flows[pos] + solve(pos, time - 1, frozenset(new_opened), ele_wait))
    return score



print("Answer 1: ", solve("AA", 30, frozenset()))
print("Answer 2: ", solve("AA", 26, frozenset(), True))
