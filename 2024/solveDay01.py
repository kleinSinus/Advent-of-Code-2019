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

# A) Compute difference of lists 
# 1. split input into two lists
left = []
right = []

for line in input:
    left.append(int(line.split()[0]))
    right.append(int(line.split()[1]))
# 2. sort the input lists ascending
lst1 = left
lst1.sort()
lst2 = right
lst2.sort()
# 3. elementwise compare the lists and compute the differences
# and output sum of differences as distance
dist = 0
for i in range(len(lst1)):
    dist += abs(lst1[i] - lst2[i])

output.write('Solution part A: ')    
output.write(str(dist) + '\n')

# B) Compute similarity score:
# 1. count occurences of numbers in left list in the right list
def countOcc(num, list):
    out = 0
    for elem in list:
        if (elem == num):
            out += 1
    return out
# 2. sum up the products of the numbers with their respective occurences as similarityScore
simScore = 0
for num in left:
    simScore += num * countOcc(num, right)

output.write('Solution part B: ')    
output.write(str(simScore) + '\n')

input.close()
output.close()