file1 = open('input.txt', 'r')
lines = file1.readlines()

times = lines[0].split(": ")[1]
times = times.split()
for i in range(len(times)):
    times[i] = int(times[i])

highScores = lines[1].split(": ")[1]
highScores = highScores.split()
for i in range(len(highScores)):
    highScores[i] = int(highScores[i])

def getCountOfWaysToWin(time, highScore):
    counter = 0
    for i in range(time):
        timeLeft = time - i
        score = (i * timeLeft)
        if score > highScore:
            counter += 1

    return counter

counts = []
for i in range(len(times)):
    counts.append(getCountOfWaysToWin(times[i], highScores[i]))

product = 1
for count in counts:
    product *= count

print(product)