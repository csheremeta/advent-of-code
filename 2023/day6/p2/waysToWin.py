file1 = open('input.txt', 'r')
lines = file1.readlines()

times = lines[0].split(": ")[1]
times = times.split()
time = ''
for i in range(len(times)):
    time += times[i]

highScores = lines[1].split(": ")[1]
highScores = highScores.split()
highScore = ''
for i in range(len(highScores)):
    highScore += highScores[i]

time = int(time)
highScore = int(highScore)

def getCountOfWaysToWin(time, highScore):
    counter = 0
    for i in range(time):
        timeLeft = time - i
        score = (i * timeLeft)
        if score > highScore:
            counter += 1

    return counter

print(getCountOfWaysToWin(time, highScore))

