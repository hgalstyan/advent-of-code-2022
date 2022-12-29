data = open("input.txt", "r").read()

def findIndex(size):
    for i in range(size, len(data)):
        if len(set(data[:i][-size:])) == size:
            return i

print("Answer 1: ", findIndex(4))
print("Answer 2: ", findIndex(14))


