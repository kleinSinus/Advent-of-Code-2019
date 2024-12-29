test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day08.txt'
outputFile += 'output/day08.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

map = []

for line in input:
    symList = []
    for symbol in line:
        if (symbol != '\n'):
            symList.append(symbol)
    map.append(symList)

frequencies = []
coordinates = []
# get frequencies
dimX = len(map[0])
dimY = len(map)
for y in range(dimY):
    for x in range(dimX):
        cell = map[y][x]
        if (cell != '.'):
            if (cell not in frequencies):
                #print('New frequency: ' + cell)
                freq = cell
                coords = [[x, y]]
                frequencies.append(freq)
                coordinates.append(coords)
            else:
                coords = [x, y]
                for i in range(len(frequencies)):
                    if frequencies[i] == cell:
                        coordinates[i].append(coords)

#for i in range(len(frequencies)):
#    print(frequencies[i])
#    print(coordinates[i])

antinodes = []

for i in range(len(frequencies)):
    for j in range(len(coordinates[i])):
        for k in range(len(coordinates[i])):
            if (j != k):
                vector = [coordinates[i][j][0] - coordinates[i][k][0], coordinates[i][j][1] - coordinates[i][k][1]]
                antinode = [coordinates[i][j][0] + vector[0], coordinates[i][j][1] + vector[1]]
                if ((antinode not in antinodes) and (antinode[0] >= 0) and (antinode[0] < dimX) and (antinode[1] >= 0) and (antinode[1] < dimY)): # only adding unique and within map area
                    antinodes.append(antinode)

antinodeNum = len(antinodes)

out = antinodeNum
print('Part 1: ' + str(out) + ' antinodes found.\n')
output.write('Part 1: ' + str(out) + ' antinodes found.\n')

antinodes = []

#print(len(frequencies))
for i in range(len(frequencies)):
    progress = i/len(frequencies)
    progPercent = int(10000*progress)/100
    print(progPercent, end='\r')
    for j in range(len(coordinates[i])):
        for k in range(len(coordinates[i])):
            if (j != k):
                vector = [coordinates[i][j][0] - coordinates[i][k][0], coordinates[i][j][1] - coordinates[i][k][1]]
                antinode = coordinates[i][j]
                while((antinode[0] >= 0) and (antinode[0] < dimX) and (antinode[1] >= 0) and (antinode[1] < dimY)): # while in map
                    #print(antinode)
                    if antinode not in antinodes: # update antinode list
                        antinodes.append(antinode)
                    antinode = [antinode[0] + vector[0], antinode[1] + vector[1]] # check next antinode

antinodeNum = len(antinodes)

out = antinodeNum
print('Part 2: ' + str(out) + ' antinodes found.\n')
output.write('Part 2: ' + str(out) + ' antinodes found.\n')


input.close()
output.close()