data = open("input.txt", "r").readlines()


def get_coords(key = 1):
    return [(idx, int(item)* key) for idx, item in enumerate(data)]

def mix(coords, times):
    _len = len(coords)
    for _ in range(times):
        for i in range(_len):
            pos, coord = [(p, coord) for p, coord in enumerate(coords) if coord[0] == i][0]
            new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

            coords.pop(pos)
            coords.insert(new_pos, coord)
    zero_pos = [p for p, item in enumerate(coords) if item[1] == 0][0]
    return coords[(zero_pos + 1000) % _len][1] + coords[(zero_pos + 2000) % _len][1] + coords[(zero_pos + 3000) % _len][1]

print("Answer 1: ", mix(get_coords(), 1))
print("Answer 2: ", mix(get_coords(811589153), 10))

