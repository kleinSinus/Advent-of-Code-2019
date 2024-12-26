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

progress1 = 0
progress2 = 0

rulesDone = False
rules = []
updates = []
for line in input:
    if (line == '\n'):
        rulesDone = True
    elif (not rulesDone):
        rules.append(line[:-1])
    else:
        if (line[-1] == '\n'):
            updates.append(line[:-1])
        else:
            updates.append(line)

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
        #print (update)
        #print ('Rule broken: ' + rule)
        return True
    else:
        return False
    
def getMiddlePage(update):
    pages = update.split(',')
    return int(pages[int(len(pages)/2)])

midPageSum = 0
for update in updates:
    progress1 += 100/len(updates)
    print('Progress part 1: ' + str(int(100*progress1)/100) + '%', end = "\r")
    breakCounter = 0
    for rule in rules:
        if (breaksRule(rule, update)):
            breakCounter += 1
    if (breakCounter == 0):
        midPageSum += getMiddlePage(update)

outA = midPageSum
output.write('Solution A: ')
output.write(str(outA) + '\n')

print('')

midPageSum2 = 0
    
from util import Graph

def fixBrokenUpdate(update, rules):
    ruleGraph = Graph()
    for rule in rules:
        left = rule.split('|')[0]
        right = rule.split('|')[1]
        ruleGraph.addVertex(left)
        ruleGraph.addVertex(right)
        ruleGraph.addEdge(left, right)
    ruleGraph.sortByIndegree()
    updateLst = update.split(',')
    result = ruleGraph.sortVertexList(updateLst)
    fixedUpdate = ''
    for elem in result:
        fixedUpdate += elem + ','
    fixedUpdate = fixedUpdate[:-1] # ditch that last comma
    return fixedUpdate

for curr in range(len(updates)):
    progress2 += 100/len(updates)
    print('Progress part 2: ' + str(int(100*progress2)/100) + '%', end = "\r")
    breakCounter = 0
    for rule in rules:
        if (breaksRule(rule, updates[curr])):
            #print('Rule ' + rule + ' broken by update ' + updates[curr] + '. Applying fix.')
            breakCounter += 1
            fix = fixBrokenUpdate(updates[curr], rules)
            if (fix == updates[curr]):
                print ('Update ' + updates[curr] + ' not fixed')
            else:
                #print (updates[curr] + ' fixed as ' + fix + '.\n')
                updates[curr] = fix # fix überschreibt vorhandenes Update
    if (breakCounter > 0):
        midPageSum2 += getMiddlePage(updates[curr])

print('')
outB = midPageSum2
output.write('Solution B: ')
output.write(str(outB) + '\n')

input.close()
output.close()