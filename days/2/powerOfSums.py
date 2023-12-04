file1 = open('input.txt', 'r')
games = file1.readlines()
powers = []

for game in games:
    mostRed = 0
    mostBlue = 0
    mostGreen = 0
    cubes = game.split(": ")[1]
    hands = cubes.split("; ")
    for hand in hands:
        colors = hand.split(", ")
        for color in colors:
            if color[1].isdigit():
                count = int(color[0:2])
            else:
                count = int(color[0:1])
            
            if "red" in color and count > mostRed:
                mostRed = count
            elif "green" in color and count > mostGreen:
                mostGreen = count
            elif "blue" in color and count > mostBlue:
                mostBlue = count

    powers.append(mostBlue * mostGreen * mostRed)

total = 0
for num in powers:
    total += num

print(total)