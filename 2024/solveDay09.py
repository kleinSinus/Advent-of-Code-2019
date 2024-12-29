test = True
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day09.txt'
outputFile += 'output/day09.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

for line in input:
    print(line)

out = 0
print('Checksum 1: ' + str(out))
output.write('Checksum 1: ' + str(out) + '\n')

out = 0
print('Checksum 2: ' + str(out))
output.write('Checksum 2: ' + str(out) + '\n')


input.close()
output.close()