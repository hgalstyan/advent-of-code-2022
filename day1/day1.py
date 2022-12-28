data = open("input.txt", "r").read()

calories = [sum(map(int, elf.split("\n"))) for elf in data.split("\n\n")]

print("Answer 1: ", max(calories))
print("Answer 2: ", sum(sorted(calories)[-3:]))