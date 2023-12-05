file1 = open('input.txt', 'r')
games = file1.readlines()
possibleGames = []
currGame = 1

for game in games:
    possible = True
    cubes = game.split(": ")[1]
    hands = cubes.split("; ")
    for hand in hands:
        colors = hand.split(", ")
        for color in colors:
            if color[1].isdigit():
                count = int(color[0:2])
            else:
                count = int(color[0:1])
            
            if "red" in color and count > 12:
                possible = False
            elif "green" in color and count > 13:
                possible = False
            elif "blue" in color and count > 14:
                possible = False
        
    if possible:
        possibleGames.append(currGame)
    
    currGame += 1

total = 0
for game in possibleGames:
    total += game

print(total)
