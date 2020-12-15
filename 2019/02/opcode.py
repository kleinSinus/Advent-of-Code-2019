def intcodeComputer(memory,pointer):
    if memory[pointer] == 1:
        memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
        pointer += 4
        intcodeComputer(memory,pointer)
    elif memory[pointer] == 2:
        memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
        pointer += 4
        intcodeComputer(memory,pointer)
    elif memory[pointer] == 99:
        pointer += 1
    else:
        return "Error: Opcode Unknown! Something went wrong!"
    return memory[0]

inputstring = open("input.txt", "r")
output = open("output.txt", "w")

inputProgram = inputstring.readline().split(',')
inputProgram = list(map(int, inputProgram))

codeInput = inputProgram.copy()

# replace values
codeInput[1] = 12
codeInput[2] = 2

# test programs
output.write("Test 1:")
output.write(str(intcodeComputer([1,0,0,0,99],0)))
output.write("\n")
output.write("Test 2:")
output.write(str(intcodeComputer([2,3,0,3,99],0)))
output.write("\n")
output.write("Test 3:")
output.write(str(intcodeComputer([2,4,4,5,99,0],0)))
output.write("\n")
output.write("Test 4:")
output.write(str(intcodeComputer([1,1,1,4,99,5,6,0,99],0)))
output.write("\n")

#restore gravity assist

output.write("Gravity Assist Restoration Value: ")
output.write(str(intcodeComputer(codeInput,0)))
output.write("\n")

# Find Config that causes output 19690720

def configFinder(desiredOutput):
    for noun in range(100):
        for verb in range(100):
            testInput = inputProgram.copy() # reset memory
            testInput[1] = noun # set noun
            testInput[2] = verb # set verb
            if (intcodeComputer(testInput,0)) == desiredOutput: # test for desired output
                return 100 * noun + verb
    return "Error: No Config of nouns and verbs between 0 and 99 return the desired output!"

output.write("Config for 19690720: ")
output.write(str(configFinder(19690720)))
output.write("\n")

inputstring.close()
output.close()