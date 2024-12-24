test = True
inputFile = ''
outputFile = ''
day = 1

if (test):
    inputFile += 'test'
    outputFile += 'test'

if (day < 10):
    inputFile += 'input/day' + '0' + str(day) + '.txt'
    outputFile += 'output/day' + '0' + str(day) + '.txt'
else:
    inputFile += 'input/day' + str(day) + '.txt'
    outputFile += 'output/day' + str(day) + '.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

output.write('bladiblub')

input.close()
output.close()