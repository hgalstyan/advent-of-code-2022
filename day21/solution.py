data = open("input.txt", "r").read().split("\n")

operations = {}
numbers = {}

def calculate(name):
    if name in numbers.keys(): return numbers[name]
    left, op, right = operations[name].split()
    return eval(str(calculate(left)) + op + str(calculate(right)))

def calculate2(name, humn):
    if name == "humn": return humn
    if name in numbers.keys(): return numbers[name]
    left, op, right = operations[name].split(" ")

    if name == "root":
        v1 = calculate2(left, humn)
        v2 = calculate2(right, humn)
        return (v1 == v2, v1, v2)

    if op == "+":
        return calculate2(left, humn) + calculate2(right, humn)
    if op == "-":
        return calculate2(left, humn) - calculate2(right, humn)
    if op == "*":
        return calculate2(left, humn) * calculate2(right, humn)
    if op == "/":
        return calculate2(left, humn) / calculate2(right, humn)


for line in data:
    name, op = line.split(": ")

    if op.isdigit():
        numbers.update({name: int(op)})
    else:
        operations.update({name: op})

print("Answer 1: ", calculate("root"))

hi = 1e20
lo = -1e20
mid = 0
while True:
    eq, l, r = calculate2("root", mid)
    if eq: break
    if l - r > 0:
        lo = mid
    else:
        hi = mid
    mid = (hi+lo)//2

print("Answer 2: ", mid)

