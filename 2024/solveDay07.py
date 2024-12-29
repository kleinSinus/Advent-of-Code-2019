test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day07.txt'
outputFile += 'output/day07.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

equations = []

for line in input:
    numbers = line.split()
    numbers[0] = numbers[0][:-1]
    equations.append(numbers)

#print(equations)

def addsUp(equation):
    target = int(equation[0])
    operands = equation[1:]
    num = len(operands) - 1 # how many operators in equation
    numPossible = 2**num # how many possible combinations
    for i in range(numPossible):
        operators = [0] * num
        j = i
        c = 0
        while (int(j) != 0):
            #print(str(i) + ': ' + str(j) + '/2= ' + str(int(j/2)) + ' R ' + str(j%2))
            op = j%2
            if (op == 1):
                operators[num-c-1] = 1
            j = int(j/2)
            c += 1
        #print(operators)
        result = int(operands[0])
        for k in range(num):
            if (operators[k] == 1):
                result *= int(operands[k+1])
            elif (operators[k] == 0):
                result += int(operands[k+1])
        if (target == result):
            return True
    return False

progress = 0
sumPossible = 0

for eq in equations:
    if (addsUp(eq)):
        sumPossible += int(eq[0])

outA = sumPossible
output.write('Solution: ' + str(outA) + '\n')

def addsUp2(equation):
    target = int(equation[0])
    operands = equation[1:]
    num = len(operands) - 1 # how many operators in equation
    numPossible = 3**num # how many possible combinations
    for i in range(numPossible):
        operators = [0] * num
        j = i
        c = 0
        while (int(j) != 0):
            op = j%3
            if (op == 1):
                operators[num-c-1] = 1
            elif (op == 2):
                operators[num-c-1] = 2
            j = int(j/3)
            c += 1
        #print(operators)
        result = int(operands[0])
        for k in range(num):
            if (operators[k] == 2):
                resultString = str(result) + operands[k+1]
                result = int(resultString)
            elif (operators[k] == 1):
                result *= int(operands[k+1])
            elif (operators[k] == 0):
                result += int(operands[k+1])
        if (target == result):
            return True
    return False

sumPossible = 0
ct = 0
for eq in equations:
    ct += 1
    progress = ct/len(equations)
    print('Progress: ' + str(int(10000*progress)/100) + '%', end = '\r')
    #print(eq)
    if (addsUp2(eq)):
        sumPossible += int(eq[0])

outB = sumPossible
output.write('Solution: ' + str(outB) + '\n')


input.close()
output.close()