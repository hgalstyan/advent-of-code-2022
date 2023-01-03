from functools import cmp_to_key

data = open("input.txt", "r").read()

def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        return -1

    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            x = compare(a[i], b[i])
            if x == 1:
                return 1
            if x == -1:
                return -1

            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1

        return -1


ans = 0

for i, block in enumerate(data.split("\n\n")):
    a, b = map(eval, block.split("\n"))
    if compare(a, b) == 1:
        ans += i + 1

print("Answer 1: ", ans)

data = data.replace("\n\n", "\n").split("\n")

lists = list(map(eval, data))
lists.append([[2]])
lists.append([[6]])
lists = sorted(lists, key=cmp_to_key(compare), reverse=True)


for i, li in enumerate(lists):
    if li == [[2]]:
        a = i + 1
    if li == [[6]]:
        b = i + 1

print("Answer 2: ", a * b)