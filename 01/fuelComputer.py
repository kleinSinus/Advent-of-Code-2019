def massToFuel(mass):
    return mass//3 - 2
    
def massToExtraFuel(mass):
    if mass <= 0:
        return 0
    else:
        return max(mass//3 - 2 + massToExtraFuel(mass//3 - 2),0)

input = open("input_a.txt", "r")
output = open("output_a.txt", "w")

fuel = 0
extraFuel = 0
for line in input:
    fuel += massToFuel(int(line))
    extraFuel += massToExtraFuel(int(line))

print("Fuel needed is ", fuel)
print("Fuel needed with considering extra fuel is ", extraFuel)
output.write(str(fuel))
output.write("\n")
output.write(str(extraFuel))

print("massToExtraFuel(100756) = ",massToExtraFuel(100756))

input.close()
output.close()