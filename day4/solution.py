data = open("input.txt", "r").read().split("\n")

counter1 =  0
counter2 =  0
for pairs in data:
    a,b = map(lambda section: tuple(map(int, section.split("-"))), pairs.split(","))
    if((a[0] - b[0])*(a[1] - b[1]) <= 0):
        counter1 += 1 
    if b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]:
        counter2 += 1 

print("Amswer 1: ", counter1)
print("Amswer 2: ", counter2)
