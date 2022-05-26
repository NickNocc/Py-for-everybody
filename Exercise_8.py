fileHandle = open('filename.type')

for line in fileHandle:
    line.rstrip()
    print(line.upper)
