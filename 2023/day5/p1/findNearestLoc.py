file1 = open('input.txt', 'r')
lines = file1.readlines()

def addNewColumn(assocArray, chart, columnNum):
    for row in chart:
        found = False
        source = int(row[columnNum-1])
        for row2 in assocArray:
            destStart = int(row2[0])
            sourceStart = int(row2[1])
            rangeLen = int(row2[2])
            if source in range(sourceStart, sourceStart+rangeLen+1):
                found = True
                difference = source - sourceStart
                dest = destStart + difference
                row.append(dest)
                pass
        if found == False:
            row.append(source)

def findNearestLocation(chart):
    locColumn = len(chart[0]) - 1
    lowestLoc = float('inf')
    for row in chart:
        if row[locColumn] < lowestLoc:
            lowestLoc = row[locColumn]
    print(locColumn)
    return lowestLoc

chart = []
seeds = lines[0].split(": ")[1]
for seed in seeds.split():
    chart.append([int(seed)])

currArray = []
entryCtr = 0
columnNum = 1
for line in lines[3:]:
    if line[0].isdigit():
        currArray.append([])
        for number in line.split():
            currArray[entryCtr].append(number)
        entryCtr += 1
    elif line[0].isalpha(): # time for new array, clear out variables
        currArray = []
        entryCtr = 0
    else: # blank line, add column to assocArray
        addNewColumn(currArray, chart, columnNum)
        columnNum += 1

# need to handle last set of associations
addNewColumn(currArray, chart, columnNum)
print(findNearestLocation(chart))
