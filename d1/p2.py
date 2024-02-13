file = open("input.txt", "r")

sum = 0
i = 0

for l in file:
    line = l

actual_lenght = len(line)
line += line
print(actual_lenght)
print(len(line))

while i <= (actual_lenght - 1):
    if line[i] == line[i + (actual_lenght//2)]:
        sum += int(line[i])
    i += 1

file.close()
print(sum)