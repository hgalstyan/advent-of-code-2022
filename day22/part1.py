data = open("input.txt", "r").read().split("\n\n")

board = data[0].split("\n")
path = data[1]

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

for cmd in commands:
    if isinstance(cmd, str):
        if cmd == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

        continue

    drow, dcol = dirs[direction]

    for _ in range(cmd):
        if (row, col) not in adj:
            break

        new_row = row + drow
        new_col = col + dcol

        if drow != 0:
            rbounds = bound_col[col]
            height = rbounds[1] - rbounds[0] + 1
            new_row = (new_row - rbounds[0]) % height + rbounds[0]

        if dcol != 0:
            cbounds = bound_row[row]
            width = cbounds[1] - cbounds[0] + 1
            new_col = (new_col - cbounds[0]) % width + cbounds[0]

        if (new_row, new_col) not in adj:
            break

        row, col = new_row, new_col


ans = 1000 * (row + 1) + 4 * (col + 1) + direction
print("Answer 1:",ans)