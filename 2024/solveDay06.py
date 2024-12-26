test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day06.txt'
outputFile += 'output/day06.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

map = []

for line in input:
    if (line[-1] == '\n'):
        map.append(line[:-1])
    else:
        map.append(line)

# 1. get obstacles as coordinates
# 2. get guard position and direction
dimY = len(map)
dimX = len(map[0])
obstacles = []
pos = []
dir = 'none'
for y in range(dimY):
    for x in range(dimX):
        if (map[y][x] == '#'):
            obstacles.append([x, y])
        elif (map[y][x] == '^'):
            pos = [x, y, 'up'] # this way even multiple guards can be monitored
        elif (map[y][x] == 'v'):
            pos = [x, y, 'down'] # this way even multiple guards can be monitored
        elif (map[y][x] == '<'):
            pos = [x, y, 'left'] # this way even multiple guards can be monitored
        elif (map[y][x] == '>'):
            pos = [x, y, 'right'] # this way even multiple guards can be monitored        
# 3. walk path
def checkObstacle(x, y, obstLst):
    for obst in obstLst:
        if([x, y] == obst):
            return True
    return False
path = [pos[:-1]]
wardenLeft = False
while not wardenLeft:
    # check next step
    obstacle = False
    if (pos[2] == 'up'):
        obstacle = checkObstacle(pos[0], pos[1]-1, obstacles)
    elif (pos[2] == 'down'):
        obstacle = checkObstacle(pos[0], pos[1]+1, obstacles)
    elif (pos[2] == 'left'):
        obstacle = checkObstacle(pos[0]-1, pos[1], obstacles)
    else:
        obstacle = checkObstacle(pos[0]+1, pos[1], obstacles)
    # turn right if an obstacle is encountered
    if obstacle:
        if (pos[2] == 'up'):
            pos[2] = 'right'
        elif (pos[2] == 'right'):
            pos[2] = 'down'
        elif (pos[2] == 'down'):
            pos[2] = 'left'
        elif (pos[2] == 'left'):
            pos[2] = 'up'
    # take next step if no obstacle is encountered
    else:
        if (pos[2] == 'up'):
            pos[1] -= 1
        elif (pos[2] == 'right'):
            pos[0] += 1
        elif (pos[2] == 'down'):
            pos[1] += 1
        elif (pos[2] == 'left'):
            pos[0] -= 1
        path.append(pos[:-1])
    # check if left
    if ((pos[0] < 0) or (pos[1] < 0) or (pos[0] >= dimX) or (pos[1] >= dimY)):
        wardenLeft = True
        path.pop()
# 4. count visited positions
def countDistinct(list):
    dist = []
    for i in range(len(list)):
        found = False
        for j in range(len(dist)):
            if(list[i] == dist[j]):
                found = True
        if not found:
            dist.append(list[i])
    #print(dist)
    return len(dist)

countPos = countDistinct(path)

out = countPos
output.write('Solution: ')
output.write(str(out) + '\n')

input.close()
output.close()