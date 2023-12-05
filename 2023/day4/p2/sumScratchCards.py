file1 = open('input.txt', 'r')
origCards = file1.readlines()
currCardNum = 0

cards = dict()
for i in range(1, len(origCards)+1):
    cards[i] = 1

for card in origCards:
    currCardNum += 1
    numMatches = 0
    winningNumbers = set()
    numbers = card.split(": ")[1]
    winners = numbers.split(" | ")[0]
    myNums = numbers.split(" | ")[1]
    for winningNumber in winners.split():
        winningNumbers.add(winningNumber)

    for number in myNums.split():
        if number in winningNumbers:
            numMatches += 1

    for i in range(1, numMatches+1):
        cards[currCardNum + i] += cards[currCardNum]

total = 0
for i in range(1, len(origCards)+1):
    total += cards[i]

print(total)