test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day03b.txt'
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
do = True
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
        elif (state == 'inY' and nextLetter == ')' and do):
            state = 'close'
            print(str(mulX) + ' * ' + str(mulY) + ' ')
            resultSum += mulX * mulY
        elif (state == 'close' and nextLetter == 'm'):
            state = 'm'
            mulX = 0
            mulY = 0
        elif (nextLetter == 'd'):
            state = 'd'
        elif (state == 'd' and nextLetter == 'o'):
            state = 'do'
        elif (state == 'do' and nextLetter == 'n'):
            state = 'don'
        elif (state == 'don' and nextLetter == '\''):
            state = 'don\''
        elif (state == 'don\'' and nextLetter == 't'):
            state = 'don\'t'
        elif (state == 'don\'t' and nextLetter == '('):
            state = 'don\'t('
        elif (state == 'don\'t(' and nextLetter == ')'):
            state = 'init'
            do = False
        elif (state == 'do' and nextLetter == '('):
            state = 'do('
        elif (state == 'do(' and nextLetter == ')'):
            state = 'init'
            do = True
        else:
            #print('abort')
            state = 'init'
            mulX = 0
            mulY = 0

outA = resultSum
output.write('Solution: ')    
output.write(str(outA) + '\n')

input.close()
output.close()