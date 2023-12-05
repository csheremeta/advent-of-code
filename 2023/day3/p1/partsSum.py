file1 = open('input.txt', 'r')
lines = file1.readlines()
inputMatrix = []
counter = 0
total = 0

for line in lines:
    inputMatrix.append([])
    for character in line:
        if character != "\n":
            inputMatrix[counter].append(character)
    counter += 1

for row in range(len(inputMatrix)):
    column = 0
    while column < len(inputMatrix[0]):
        if inputMatrix[row][column].isdigit():
            useNum = False
            currNum = 0
            while column < len(inputMatrix[0]) and inputMatrix[row][column].isdigit():
                currNum = currNum * 10
                currNum = currNum + int(inputMatrix[row][column])
                if useNum == False:
                    if row-1 >= 0:
                        if not inputMatrix[row-1][column].isalnum() and inputMatrix[row-1][column] != '.':
                            useNum = True
                        if column-1 >= 0:
                            if not inputMatrix[row-1][column-1].isalnum() and inputMatrix[row-1][column-1] != '.':
                                useNum = True
                        if column+1 < len(inputMatrix[0]):
                            if not inputMatrix[row-1][column+1].isalnum() and inputMatrix[row-1][column+1] != '.':
                                useNum = True
                    if row+1 < len(inputMatrix):
                        if not inputMatrix[row+1][column].isalnum() and inputMatrix[row+1][column] != '.':
                            useNum = True
                        if column-1 >= 0:
                            if not inputMatrix[row+1][column-1].isalnum() and inputMatrix[row+1][column-1] != '.':
                                useNum = True
                        if column+1 < len(inputMatrix[0]):
                            if not inputMatrix[row+1][column+1].isalnum() and inputMatrix[row+1][column+1] != '.':
                                useNum = True
                    if column-1 >= 0:
                        if not inputMatrix[row][column-1].isalnum() and inputMatrix[row][column-1] != '.':
                            useNum = True
                    if column+1 < len(inputMatrix[0]):
                        if not inputMatrix[row][column+1].isalnum() and inputMatrix[row][column+1] != '.':
                            useNum = True
                column += 1
            
            if useNum:
                total += currNum
        column += 1

print(total)