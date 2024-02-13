file = open("input.txt", "r")

checksum = 0

for line in file:
    line = line.rstrip()
    line = line.split()
    print(line)
    line = [int(i) for i in line]
    print(line)
    checksum += (int(max(line)) - int(min(line)))

file.close()
print(checksum)