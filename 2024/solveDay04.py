test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day04.txt'
outputFile += 'output/day04.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

grid = []
# make matrix
for line in input:
    lineArray = []
    for letter in line:
        lineArray.append(letter)
    grid.append(lineArray)

for i in range(len(grid)):
    content = grid[i]
    if(content[-1] == '\n'):
        grid[i] = content[:-1] # letzes Zeichen ist der Zeilenumbruch, der soll nicht ins Grid

dimX = len(grid[0])
dimY = len(grid)
count = 0

for y in range(dimY): # i is row index
    for x in range(dimX): # j is col index
        if (grid[y][x] == 'X'):
            # try north
            if (y > 2): # no northbound match possible for y indexes lesser 3
                if (grid[y-1][x] == 'M' and grid[y-2][x] == 'A' and grid[y-3][x] == 'S'):
                    count += 1
            # try northeast
            if (y > 2 and x < (dimX-3)): # no northbound match possible for y indexes lesser 3, no eastbound matches up to 3 away from border
                if (grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S'):
                    count += 1
            # try east
            if (x < (dimX-3)): # no eastbound matches up to 3 away from border
                if (grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S'):
                    count += 1
            # try southeast
            if (y < (dimY-3) and x < (dimX-3)): # no southbound matches up to 3 away from border, no eastbound matches up to 3 away from border
                if (grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == 'S'):
                    count += 1
            # try south
            if (y < (dimY-3)): # no southbound matches up to 3 away from border
                if (grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S'):
                    count += 1
            # try southwest
            if (y < (dimY-3) and x > 2): # no southbound matches up to 3 away from border, no westbound matches up to 3 away from border
                if (grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S'):
                    count += 1
            # try west
            if (x > 2): # no westbound matches up to 3 away from border
                if (grid[y][x-1] == 'M' and grid[y][x-2] == 'A' and grid[y][x-3] == 'S'):
                    count += 1
            # try north west
            if (y > 2 and x > 2): # no westbound matches up to 3 away from border, no northbound matches up to 3 away from border
                if (grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == 'S'):
                    count += 1

outA = count
output.write('XMAS found: ')    
output.write(str(outA) + '\n')

countB = 0
for y in range(dimY): # i is row index
    for x in range(dimX): # j is col index
        if (grid[y][x] == 'A'):
            if (y > 0 and y < (dimY-1) and x > 0 and x < (dimX-1)): # Letter A can't be on the outer border
                if (grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'S'):
                    countB += 1
                if (grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'S'):
                    countB += 1
                if (grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'M'):
                    countB += 1
                if (grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'M'):
                    countB += 1

outB = countB
output.write('X-MAS found: ')
output.write(str(outB) + '\n')

input.close()
output.close()