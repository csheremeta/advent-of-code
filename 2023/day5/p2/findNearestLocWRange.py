file1 = open('input.txt', 'r')
lines = file1.readlines()

seeds = []
seedsToSoils = []
soilsToFertilizers = []
fertilizersToWaters = []
watersToLights = []
lightsToTemperatures = []
temperaturesToHumidities = []
humiditiesToLocations = []

seedLine = lines[0].split(": ")[1]
seedLine = seedLine.split()
while len(seedLine) > 0:
    seeds.append([int(seedLine[0]), int(seedLine[1])])
    seedLine.remove(seedLine[0])
    seedLine.remove(seedLine[0])

# hard-coding line numbers because I'm tired of parsing files
# could come back and do a cleaner solution
for line in lines[3:20]:
    seedsToSoils.append(line.split())
for line in seedsToSoils:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[22:53]:
    soilsToFertilizers.append(line.split())
for line in soilsToFertilizers:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[55:94]:
    fertilizersToWaters.append(line.split())
for line in fertilizersToWaters:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[96:113]:
    watersToLights.append(line.split())
for line in watersToLights:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[115:134]:
    lightsToTemperatures.append(line.split())
for line in lightsToTemperatures:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[136:166]:
    temperaturesToHumidities.append(line.split())
for line in temperaturesToHumidities:
    for i in range(len(line)):
        line[i] = int(line[i])

for line in lines[168:206]:
    humiditiesToLocations.append(line.split())
for line in humiditiesToLocations:
    for i in range(len(line)):
        line[i] = int(line[i])

def transformOldRes(oldResNum, newToOldArr):
    for line in newToOldArr:
        if line[1] <= oldResNum <= line[1]+line[2]:
            offset = oldResNum - line[1]
            return line[0]+offset
    return oldResNum


def findNearestLocation():
    location = 0
    found = False
    while not found:
        humidity = transformOldRes(location, humiditiesToLocations)
        temperature = transformOldRes(humidity, temperaturesToHumidities)
        light = transformOldRes(temperature, lightsToTemperatures)
        water = transformOldRes(light, watersToLights)
        fertilizer = transformOldRes(water, fertilizersToWaters)
        soil = transformOldRes(fertilizer, soilsToFertilizers)
        seed = transformOldRes(soil, seedsToSoils)
        for line in seeds:
            if line[0] <= seed <= (line[0]+line[1]):
                print(seed)
                print(soil)
                print(fertilizer)
                print(water)
                print(light)
                print(temperature)
                print(humidity)
                print(location)
                found = True
                return location
        location += 1

print(findNearestLocation())