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
    msg = ''
    for i in range(len(report)-1):
        stepDiff = int(report[i+1]) - int(report[i])
        if (stepDiff == 0):
            msg = 'Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is neither an increase nor a decrease.'
            isSafe = False
            break
        elif (stepDiff > 0):
            if (not isIncrease):
                increaseFirst = i
                isIncrease = True
            if (stepDiff > 3):
                msg = 'Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is an increase of ' + str(stepDiff) + '.'
                isSafe = False
                break
        else:
            if (not isDecrease):
                decreaseFirst = i
                isDecrease = True
            if (stepDiff < -3):
                msg = 'Unsafe, because `' + str(report[i]) + ' ' + str(report[i+1]) + '` is a decrease of ' + str(abs(stepDiff)) + '.'
                isSafe = False
                break
        if (isIncrease and isDecrease):
            msg = 'Unsafe, because `' + str(report[increaseFirst]) + ' ' + str(report[increaseFirst+1]) + '` is increasing but `' + str(report[decreaseFirst]) + ' ' + str(report[decreaseFirst+1]) + '` is decreasing.'
            isSafe = False
            break
        if (isIncrease and not isDecrease and (i == len(report)-2)):
            isIncreaseOnly = True
        if (isDecrease and not isIncrease and (i == len(report)-2)):
            isDecreaseOnly = True
        if (isIncreaseOnly and isSafe):
            msg = 'Safe because the levels are all increasing by 1, 2, or 3.'
        if (isDecreaseOnly and isSafe):
            msg = 'Safe because the levels are all decreasing by 1, 2, or 3.'
    return [isSafe, msg]
# 2. count safe reports
safeCount = 0
for report in reports:
    if (isSafeReport(report)[0]):
        safeCount += 1
    print(isSafeReport(report)[1])

outA = safeCount
output.write('Solution part A: ')    
output.write(str(outA) + '\n')

# B) Problem Dampener
# 1. omit one Level from bad reports
def omitLvl(report, lvl):
    out = []
    for i in range(len(report)):
        if (i != lvl):
            out.append(report[i])
    return out
# 2. and check for possibly safe reports among the unsafe
for report in reports:
    print (report)
    if (not isSafeReport(report)[0]):
        for lv in range(len(report)):
            if (isSafeReport(omitLvl(report, lv))[0]):
                safeCount += 1
                print ("Safe, by removing level " + str(lv+1) + ": " + str(report[lv]) + ".")
                break
    else:
        print ('Safe without removing any level.')
            

    

outB = safeCount
output.write('Solution part B: ')    
output.write(str(outB) + '\n')

input.close()
output.close()