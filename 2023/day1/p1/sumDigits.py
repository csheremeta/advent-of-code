file1 = open('day-1-list.txt', 'r')
lines = file1.readlines()
nums = []

for string in lines:    
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