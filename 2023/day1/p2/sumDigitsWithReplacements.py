file1 = open('day-1-list.txt', 'r')
file2 = open('day-1-list-replacements.txt', 'w')
lines = file1.readlines()
nums = []

for string in lines:
    newStr1 = string.replace('one', 'o1e')
    newStr2 = newStr1.replace('two', 't2o')
    newStr3 = newStr2.replace('three', 't3e')
    newStr4 = newStr3.replace('four', 'f4r')
    newStr5 = newStr4.replace('five', 'f5e')
    newStr6 = newStr5.replace('six', 's6x')
    newStr7 = newStr6.replace('seven', 's7n')
    newStr8 = newStr7.replace('eight', 'e8t')
    newStr9 = newStr8.replace('nine', 'n9e')
    file2.write(newStr9)

file2.close()
file2 = open('day-1-list-replacements.txt', 'r')
lines2 = file2.readlines()

for string in lines2:    
    leftPtr = 0
    rightPtr = len(string)-1
    while not string[leftPtr].isdigit() and leftPtr < len(string):
        leftPtr += 1
    while not string[rightPtr].isdigit() and rightPtr >= 0:
        rightPtr -= 1
    
    nums.append((int(string[leftPtr]) * 10) + int(string[rightPtr]))

total = 0
for number in nums:
    total += number

print(total)