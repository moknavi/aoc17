file = open("input.txt", "r")

checksum = 0

for line in file:
    line = line.rstrip()
    line = line.split()
    line = [int(i) for i in line]
    print(line)
    for i in line:
        for j in line:
            if (i % j) == 0 and i > j:
                checksum += (i // j)

file.close()
print(checksum)