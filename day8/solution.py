data = open("input.txt", "r").read().split("\n")

trees = [[*map(int, line)] for line in data]
visible = n = 2 * (len(trees[0]) + len(trees) - 2)
scores = []

for y in range(1, len(trees)-1):
    for x in range(1, len(trees[0])-1):

        col = [t[x] for t in trees]
        row = trees[y]

        left = row[:x]
        right = row[x + 1 :]
        top = col[:y]
        bottom = col[y + 1 :]

        tree = trees[y][x]

        if tree > min(max(left), max(right), max(top), max(bottom)):
            visible += 1
        
        score = 1
        for lst in (left[::-1], right, top[::-1], bottom):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                else:
                    tracker += 1
                    break

            score *= tracker

        
        scores.append(score)


print("Answer 1: ", visible)
print("Answer 2: ", max(scores))
