data = open("input.txt", "r").read().split("\n\n")

board = data[0].split("\n")
path = data[1]

debug = False

idx = 0
commands = []
cur_num = ""
for idx in range(len(path)):
    if path[idx].isdigit():
        cur_num += path[idx]

    else:

        commands.append(int(cur_num))
        cur_num = ""
        commands.append(path[idx])

if cur_num != "":
    commands.append(int(cur_num))

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


nrows = len(board)
ncols = max([len(row) for row in board])

bound_row = [[ncols, -1] for _ in range(nrows)]
bound_col = [[nrows, -1] for _ in range(ncols)]

adj = set()
for row, line in enumerate(board):
    for col in range(len(line)):
        c = line[col]
        if c == ".":
            adj.add((row, col))

        if c in [".", "#"]:
            bound_row[row][0] = min(bound_row[row][0], col)
            bound_row[row][1] = max(bound_row[row][1], col)
            bound_col[col][0] = min(bound_col[col][0], row)
            bound_col[col][1] = max(bound_col[col][1], row)


direction = 0
row = 0
col = bound_row[0][0]

SCALE = 50  

edge_map = [
    [[(0, 1), (0, 2), "^"], [(3, 0), (4, 0), "<"]],  
    [[(0, 2), (0, 3), "^"], [(4, 0), (4, 1), "v"]],  
    [[(0, 3), (1, 3), ">"], [(3, 2), (2, 2), ">"]],  
    [[(1, 2), (1, 3), "v"], [(1, 2), (2, 2), ">"]],  
    [[(3, 1), (3, 2), "v"], [(3, 1), (4, 1), ">"]],  
    [[(2, 0), (3, 0), "<"], [(1, 1), (0, 1), "<"]],  
    [[(2, 0), (2, 1), "^"], [(1, 1), (2, 1), "<"]]   
]


def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


def add(a, b):
    a_copy = list(a)
    for i in range(len(a)):
        a_copy[i] += b[i]
    return tuple(a_copy)


def mult(a, k):
    a_copy = list(a)
    for i in range(len(a)):
        a_copy[i] *= k
    return tuple(a_copy)


for i in range(len(edge_map)):
    for j in range(2):
        edge_map[i][j][2] = ">v<^".index(edge_map[i][j][2])
        for k in range(2):
            edge_map[i][j][k] = mult(edge_map[i][j][k], SCALE)


def along_edge_dir(edge):
    start, end, _ = edge
    return sign(end[0] - start[0]), sign(end[1] - start[1])


# Off-by-one errors if edge is backwards
for i in range(len(edge_map)):
    for j in range(2):
        edge = edge_map[i][j]
        along = along_edge_dir(edge)

        if along[0] < 0 or along[1] < 0:
            edge[0] = add(edge[0], along)
            edge[1] = add(edge[1], along)

        edge_map[i][j] = edge


def off_edge(point, edge, direction):
    start, end, edge_dir = edge

    if edge_dir != direction:
        return None

    if direction in [2, 3]:
        start = add(start, dirs[direction])
        end = add(end, dirs[direction])

    idx = 0

    drow, dcol = along_edge_dir(edge) 
    row, col = start[0], start[1]

    for idx in range(SCALE):
        if (row, col) == point:
            return idx

        row += drow
        col += dcol

    return None


def point_at(edge, idx):
    assert idx < SCALE

    start, end, edge_dir = edge
    drow, dcol = along_edge_dir(edge)

    if edge_dir in [0, 1]:
        start = add(start, mult(dirs[edge_dir], -1))
        end = add(end, mult(dirs[edge_dir], -1))

    return add(start, mult((drow, dcol), idx))


def wrap(row, col, direction):
    idx = None

    for e1, e2 in edge_map:
        idx = off_edge((row, col), e1, direction)
        if isinstance(idx, int):
            break

        idx = off_edge((row, col), e2, direction)
        if isinstance(idx, int):
            e1, e2 = e2, e1 
            break

    if idx == None:
        return (row, col, direction)

    assert idx == off_edge((row, col), e1, direction)

    new_point = point_at(e2, idx)

    new_direction = [2, 3, 0, 1][e2[2]]

    return new_point[0], new_point[1], new_direction


for cmd in commands:

    if isinstance(cmd, str):
        if cmd == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        continue

    for _ in range(cmd):
        drow, dcol = dirs[direction]

        if (row, col) not in adj:
            break

        new_row, new_col = row + drow, col + dcol

        new_new_row, new_new_col, new_direction = wrap(new_row, new_col, direction)

        if (new_new_row, new_new_col) not in adj:
            break

        row, col = new_new_row, new_new_col
        direction = new_direction


ans = 1000 * (row + 1) + 4 * (col + 1) + direction
print("Answer 2: ", ans)