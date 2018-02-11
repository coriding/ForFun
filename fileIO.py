myFile = open("./testfile.txt", 'r')

for line in myFile:
    print(line, end='')

myFile.close()