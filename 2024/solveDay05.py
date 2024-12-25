test = True
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day05.txt'
outputFile += 'output/day05.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

outB = 0
output.write('Solution: ')
output.write(str(outB) + '\n')

input.close()
output.close()