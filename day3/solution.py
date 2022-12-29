data = open("input.txt", "r").read().split("\n")

#38 for uppercase
#96 for lowercase
priority1 = 0
for d in data:
    half = len(d)//2
    char = (set(d[:half]) & set(d[half:])).pop()
    priority1 += ord(char) - (96 if char.islower() else 38) 


priority2 = 0
for i in range(0, len(data), 3):
    r1,r2,r3 = map(set, data[i: i + 3])
    char = (r1 & r2 & r3).pop()
    priority2 += ord(char) - (96 if char.islower() else 38) 

print("Answer 1: ", priority1)
print("Answer 2: ", priority2)