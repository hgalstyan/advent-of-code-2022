# A,X - Rock - 1
# B,Y - Paper - 2 
# C,Z - Scissor - 3
# X, Loss - 0
# Y, Draw - 3
# Z, Win - 6

data = open("input.txt", "r").read().split("\n")

#[A, B, C]
arr1 = [[3, 0, 6],
       [6, 3, 0],
       [0, 6, 3]]

# row1 - loss
# row2 - draw
# row3 - win
arr2 = [[3, 1, 2], 
        [4, 5, 6],
        [8, 9, 7]]

map_of_index = {"A": 1,"B": 2, "C": 3, "X": 0, "Y": 1, "Z": 2}
points1 = 0
points2 = 0

for round in data:
    choices = round.split(" ")
    x,y = map_of_index.get(choices[1]), map_of_index.get(choices[0])
    points1 += arr1[x][y] + x + 1
    points2 += arr2[x][y-1]


print("Answer 1: ", points1)
print("Answer 2: ", points2)
