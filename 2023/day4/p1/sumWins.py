file1 = open('input.txt', 'r')
cards = file1.readlines()
scores = []

for card in cards:
    numMatches = 0
    currScore = 0
    winningNumbers = set()
    numbers = card.split(": ")[1]
    winners = numbers.split(" | ")[0]
    myNums = numbers.split(" | ")[1]
    for winningNumber in winners.split():
        winningNumbers.add(winningNumber)
    
    for number in myNums.split():
        if number in winningNumbers:
            if currScore == 0:
                currScore = 1
            else:
                currScore = currScore * 2

    scores.append(currScore)

total = 0
for score in scores:
    total += score

print(total)