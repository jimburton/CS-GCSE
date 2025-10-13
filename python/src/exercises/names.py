
names = {}

with open('names.txt') as file:
    for line in file:
        name = line[:-1]
        if name in names:
            names[name] += 1
        else:
            names[name] = 1

print(names)
