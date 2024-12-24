test = True
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day03.txt'
outputFile += 'output/day03.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

# Part A: Parse Multiplications
def isNum(letter):
    if (letter == '0' or letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9'):
        return True
    else:
        return False
       
state = 'init'
seqStart = 0
seqEnd = 0
mulX = 0
mulY = 0
resultSum = 0
for inputLine in input:
    for nextLetter in inputLine:
        if (state == 'init' and nextLetter == 'm'):
            state = 'm'
        elif (state == 'm' and nextLetter == 'u'):
            state = 'mu'
        elif (state == 'mu' and nextLetter == 'l'):
            state = 'mul'
        elif (state == 'mul' and nextLetter == '('):
            state = 'open'
        elif (state == 'open' and isNum(nextLetter)):
            state = 'inX'
            mulX = 10 * mulX + int(nextLetter)
        elif (state == 'inX' and isNum(nextLetter)):
            state = 'inX'
            mulX = 10 * mulX + int(nextLetter)
        elif (state == 'inX' and nextLetter == ','):
            state = 'comma'
        elif (state == 'comma' and isNum(nextLetter)):
            state = 'inY'
            mulY = 10 * mulY + int(nextLetter)
        elif (state == 'inY' and isNum(nextLetter)):
            state = 'inY'
            mulY = 10 * mulY + int(nextLetter)
        elif (state == 'inY' and nextLetter == ')'):
            state = 'close'
            print(str(mulX) + ' * ' + str(mulY) + ' ')
            resultSum += mulX * mulY
        elif (state == 'close' and nextLetter == 'm'):
            state = 'm'
            mulX = 0
            mulY = 0
        else:
            #print('abort')
            state = 'init'
            mulX = 0
            mulY = 0

outA = resultSum
output.write('Solution part A: ')    
output.write(str(outA) + '\n')

# B) Problem Dampener

outB = 0
output.write('Solution part B: ')    
output.write(str(outB) + '\n')

input.close()
output.close()