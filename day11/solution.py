from collections import deque
from math import lcm

data = open("input.txt", "r").read().split("\n")

def parse_data():
    d = []
    for i in range(0, len(data), 7):
        initial_data = {}
        initial_data["items"] = deque([*map(int, data[i+1].split(":")[1].strip().split(", "))])

        match data[i+2].split("= ")[1].strip().split():
            case ["old", "+", "old"]:
                ope = lambda x: x + x
            case ["old", "+", val]:
                ope = lambda x, val=int(val): x + val
            case ["old", "*", "old"]:
                ope = lambda x: x * x
            case ["old", "*", val]:
                ope = lambda x, val=int(val): x * val
        
        target = [int(data[i+5].split("monkey")[1].strip()), int(data[i+4].split("monkey")[1].strip())]  # [if_false, if_true]

        initial_data["operation"] = ope
        initial_data["test"] = int(data[i+3].split("by ")[1])
        initial_data["target"] = target
        initial_data["times"] = 0
        d.append(initial_data)
    return d


def execute(data, times, _lambda):
    for _ in range(times):
        for monkey in data:
            while monkey["items"]:
                monkey["times"] += 1
                item = monkey["items"].popleft()
                item = monkey["operation"](item)
                item = _lambda(item)
                test = item % monkey["test"] == 0
                target = monkey["target"][test]
                data[target]["items"].append(item)
    return data

data1 = parse_data()
_lambda = lambda x: x//3
part1 = execute(data1, 20, _lambda)

data2 = parse_data()
test_lcm = lcm(*[i["test"] for i in data2])
_lambda = lambda x: x%test_lcm
part2 = execute(parse_data(), 10000, _lambda)



times1 = sorted(m["times"] for m in part1)
times2 = sorted(m["times"] for m in part2)

print("Answer 1: ", times1[-1] * times1[-2])
print("Answer 2: ", times2[-1] * times2[-2])






