file1 = open('input.txt', 'r')
lines = file1.readlines()
inputMatrix = []
counter = 0
ratios = []
total = 0

def findNum(inputMatrix, row, column):
    startIdx = column
    endIdx = column
    num = 0
    while startIdx > 0 and inputMatrix[row][startIdx-1].isdigit():
        startIdx -= 1
    while endIdx < (len(inputMatrix[row])-1) and inputMatrix[row][endIdx+1].isdigit():
        endIdx += 1
    for i in range(startIdx, endIdx+1):
        num = (num * 10) + int(inputMatrix[row][i])
    return num
    
def checkStar(inputMatrix, row, column):
    numList = []
    if column-1 >= 0 and inputMatrix[row][column-1].isdigit():
        numList.append(findNum(inputMatrix, row, column-1))
    if column+1 < len(inputMatrix[row]) and inputMatrix[row][column+1].isdigit():
        numList.append(findNum(inputMatrix, row, column+1))
    if row-1 >= 0:
        if not inputMatrix[row-1][column].isdigit():
            if column-1 >= 0 and inputMatrix[row-1][column-1].isdigit():
                numList.append(findNum(inputMatrix, row-1, column-1))
            if column+1 < len(inputMatrix[row]) and inputMatrix[row-1][column+1].isdigit():
                numList.append(findNum(inputMatrix, row-1, column+1))
        else: # if character directly above star is a number
            numList.append(findNum(inputMatrix, row-1, column))
    if row+1 < len(inputMatrix):
        if not inputMatrix[row+1][column].isdigit():
            if column-1 >= 0 and inputMatrix[row+1][column-1].isdigit():
                numList.append(findNum(inputMatrix, row+1, column-1))
            if column+1 < len(inputMatrix[row]) and inputMatrix[row+1][column+1].isdigit():
                numList.append(findNum(inputMatrix, row+1, column+1))
        else: # if character directly below star is a number
            numList.append(findNum(inputMatrix, row+1, column))
    if len(numList) == 2:
        ratios.append(numList[0] * numList[1])

for line in lines:
    inputMatrix.append([])
    for character in line:
        if character != "\n":
            inputMatrix[counter].append(character)
    counter += 1


for row in range(len(inputMatrix)):
    for column in range(len(inputMatrix[row])):
        if inputMatrix[row][column] == '*':
            checkStar(inputMatrix, row, column)

for num in ratios:
    total += num

print(total)