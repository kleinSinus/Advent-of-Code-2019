test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day01.txt'
outputFile += 'output/day01.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

# 1. split input into two lists
lst1 = []
lst2 = []

for line in input:
    lst1.append(int(line.split()[0]))
    lst2.append(int(line.split()[1]))
# 2. sort the input lists ascending
lst1.sort()
lst2.sort()
# 3. elementwise compare the lists and compute the differences
# and output sum of differences as distance
dist = 0
for i in range(len(lst1)):
    dist += abs(lst1[i] - lst2[i])
    
output.write(str(dist))

input.close()
output.close()