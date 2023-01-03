data = open("input.txt", "r").read().split("\n")

sand_source = 500, 0

def parse():
    filled = set()
    for line in data:
        coords = []

        for str_coord in line.split(" -> "):
            x, y = map(int, str_coord.split(","))
            coords.append((x, y))

        for i in range(1, len(coords)):
            cx, cy = coords[i]
            px, py = coords[i - 1]

            if cy != py:
                assert cx == px
                for y in range(min(cy, py), max(cy, py) + 1):
                    filled.add((cx, y))

            if cx != px:
                assert cy == py
                for x in range(min(cx, px), max(cx, px) + 1):
                    filled.add((x, cy))
    return filled

filled = parse()
max_y = max([coord[1] for coord in filled])

def simulate_sand():
    global filled
    x, y = 500, 0

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        # Everything filled, come to rest
        filled.add((x, y))
        return True

    return False

filled2 = parse()

def simulate_sand2():
    global filled2
    x, y = 500, 0

    if (x, y) in filled:
        return (x, y)

    while y <= max_y:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x - 1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        # Everything filled, come to rest
        break

    return (x, y)

def part1():
    ans = 0
    while True:
        res = simulate_sand()
        if not res:
            break
        ans += 1
    return ans

def part2():
    ans = 0
    while True:
        x, y = simulate_sand2()
        filled2.add((x, y))
        ans += 1

        if (x, y) == (500, 0):
            break
    return ans


print("Answer 1: ", part1())
print("Answer 2: ", part2())
