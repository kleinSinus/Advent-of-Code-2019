test = False
inputFile = ''
outputFile = ''

if (test):
    inputFile += 'test'
    outputFile += 'test'

inputFile += 'input/day02.txt'
outputFile += 'output/day02.txt'

input = open(inputFile, "r")
output = open(outputFile, "w")

# Part A: Count safe reports
reports = []
for line in input:
    reports.append(line.split())
# 1. determine report safety
def isSafeReport(report):
    isIncrease = False
    isDecrease = False
    isIncreaseOnly = False
    isDecreaseOnly = False
    increaseFirst = 0
    decreaseFirst = 0
    isSafe = True
    for i in range(len(report)-1):
        stepDiff = int(report[i+1]) - int(report[i])
        if (stepDiff == 0):
            print ('Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is neither an increase nor a decrease.')
            isSafe = False
            break
        elif (stepDiff > 0):
            if (not isIncrease):
                increaseFirst = i
                isIncrease = True
            if (stepDiff > 3):
                print ('Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is an increase of ' + str(stepDiff) + '.')
                isSafe = False
                break
        else:
            if (not isDecrease):
                decreaseFirst = i
                isDecrease = True
            if (stepDiff < -3):
                print ('Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is a decrease of ' + str(abs(stepDiff)) + '.')
                isSafe = False
                break
        if (isIncrease and isDecrease):
            print ('Unsafe, because `' + str(report[increaseFirst]) + ' ' + str(report[increaseFirst+1]) + '` is increasing but `' + str(report[decreaseFirst]) + ' ' + str(report[decreaseFirst+1]) + '` is decreasing.')
            isSafe = False
            break
        if (isIncrease and not isDecrease and (i == len(report)-2)):
            isIncreaseOnly = True
        if (isDecrease and not isIncrease and (i == len(report)-2)):
            isDecreaseOnly = True
        if (isIncreaseOnly and isSafe):
            print ('Safe because the levels are all increasing by 1, 2, or 3.')
        if (isDecreaseOnly and isSafe):
            print ('Safe because the levels are all decreasing by 1, 2, or 3.')
    return isSafe
# 2. count safe reports
safeCount = 0
for report in reports:
    if (isSafeReport(report)):
        safeCount += 1

outA = safeCount
output.write('Solution part A: ')    
output.write(str(outA) + '\n')


outB = 0
output.write('Solution part B: ')    
output.write(str(outB) + '\n')

input.close()
output.close()