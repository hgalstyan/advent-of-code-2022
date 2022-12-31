data = open("input.txt", "r").read().split("\n")

sum = 0
cycle = 0
x = 1
checkpoint = [20,60,100,140,180,220]
crt = list("." * 240)
sprite_pos = [i for i in [x - 1, x, x + 1] if i >= 0]

for row in data:
    if row == "noop":
        step = 1
        add_x = 0
    else:
        _, num = row.split()
        add_x = int(num)
        step = 2

    for c in checkpoint:
        if cycle < c <= cycle + step:
            sum += x * c
    
    for i in range(step):
        pos = cycle + i
        if pos % 40 in sprite_pos:
            crt[pos] = "#"
    
    x += add_x
    cycle += step
    sprite_pos = [i for i in [x - 1, x, x + 1] if i >= 0]    



print("Answer 1: ",sum)
print("Answer 2: ")
for i in range(0, 240, 40):
    print("".join(crt[i : i + 40]))
