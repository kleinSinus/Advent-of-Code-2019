import time

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
start = []
dir = 'none'
for y in range(dimY):
    for x in range(dimX):
        if (map[y][x] == '#'):
            obstacles.append([x, y])
        elif (map[y][x] == '^'):
            start = [x, y, 'up'] 
        elif (map[y][x] == 'v'):
            start = [x, y, 'down'] 
        elif (map[y][x] == '<'):
            start = [x, y, 'left'] 
        elif (map[y][x] == '>'):
            start = [x, y, 'right']      
# 3. walk path
def checkObstacle(x, y, obstLst):
    for obst in obstLst:
        if([x, y] == obst):
            return True
    return False
pos = start.copy()
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
output.write('The warden visits ')
output.write(str(out) + ' distinct positions. \n')

def hasVisited(pos, path):
    #print('Looking for position ' + str(pos) + ' in path ' + str(path))
    for step in path:
        if step == pos:
            #print(str(step) + ' is the same as ' + str(pos))
            return True
    return False

def renderTime(time):
    if time < 60:
        return str(time) + ' sec'
    elif time < 3600:
        minutes = int(time/60)
        seconds = time - (minutes * 60)
        return str(minutes) + ' min ' + str(seconds) + ' sec'
    else:
        hours = int(time/3600)
        minutes = int((time-(hours*3600))/60)
        seconds = time - (hours*3600 + minutes * 60)
        return str(hours) + ' h ' + str(minutes) + ' min ' + str(seconds) + ' sec'

startTime = time.time()
progress = 0
countLoop = 0
for y in range(dimY):
    for x in range(dimX):
        progress += 1/(dimX*dimY)
        elapsedTime = time.time() - startTime
        estimatedTime = elapsedTime/progress
        leftTime = estimatedTime - elapsedTime
        print('Progress: ' + str(int(100*progress)/100) + '%, Time elapsed: ' + renderTime(int(elapsedTime)) + ', Time left (estimate): ' + renderTime(int(leftTime)), end='\r')
        nu = [[x, y]]
        nuObst = obstacles + nu
        pos = start.copy()
        #print (pos)
        path = [pos.copy()] # this time the direction the warden is facing is important during the path
        wardenLeft = False
        loopEncountered = False
        while not (wardenLeft or loopEncountered):
            # check next step
            obstacle = False
            if (pos[2] == 'up'):
                obstacle = checkObstacle(pos[0], pos[1]-1, nuObst)
            elif (pos[2] == 'down'):
                obstacle = checkObstacle(pos[0], pos[1]+1, nuObst)
            elif (pos[2] == 'left'):
                obstacle = checkObstacle(pos[0]-1, pos[1], nuObst)
            else:
                obstacle = checkObstacle(pos[0]+1, pos[1], nuObst)
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
            # check if left
            if ((pos[0] < 0) or (pos[1] < 0) or (pos[0] >= dimX) or (pos[1] >= dimY)):
                wardenLeft = True
                #print ('Warden left.')
            # check if loop
            elif hasVisited(pos, path):
                loopEncountered = True
                countLoop += 1
                #print('Loop for introducing new obstacle at ' + str(nu[0]))
            else:
                path.append(pos.copy())

out = countLoop
output.write(str(out) + ' loops can be introduced using a new obstacle. \n')

input.close()
output.close()