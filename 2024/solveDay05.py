test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day05.txt'
outputFile += 'output/day05.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

rulesDone = False
rules = []
updates = []
for line in input:
    if (line == '\n'):
        rulesDone = True
    elif (not rulesDone):
        rules.append(line[:-1])
    else:
        updates.append(line[:-1])

def breaksRule(rule, update):
    #print ('Checking update ' + update  + ' against rule ' + rule  + ':')
    left = rule.split('|')[0]
    right = rule.split('|')[1]
    pages = update.split(',')
    #print(pages)
    indexLeft = len(update) # an out of bounds index shows this index hasn't been set
    indexRight = len(update)
    for i in range(len(pages)):
        #print(pages[i] + ': ' + left + '|' + right)
        if (pages[i] == left):
            #print ('Found left')
            indexLeft = i
        elif (pages[i] == right):
            #print ('Found right')
            indexRight = i
    if (indexRight == len(update) or indexLeft == len(update)): # one page from the rule is not in this update
        return False
    elif (indexLeft > indexRight): # left side of rule comes after right side in update
        print (update)
        print ('Rule broken: ' + rule)
        return True
    else:
        return False
    
def getMiddlePage(update):
    pages = update.split(',')
    return int(pages[int(len(pages)/2)])

midPageSum = 0
for update in updates:
    breakCounter = 0
    for rule in rules:
        if (breaksRule(rule, update)):
            breakCounter += 1
    if (breakCounter == 0):
        midPageSum += getMiddlePage(update)

outB = midPageSum
output.write('Solution: ')
output.write(str(outB) + '\n')

input.close()
output.close()