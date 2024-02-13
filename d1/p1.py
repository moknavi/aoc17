file = open("input.txt", "r")

sum = 0
for line in file:
    line += line[0]

    for i, c in enumerate(line):
        if i == len(line) - 1:
            break
        if c == line[i + 1]:
            sum += int(c)

file.close()
print(sum)