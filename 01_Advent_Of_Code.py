import math

inputfile = open("C:\\Users\\m-wie\\OneDrive\\Desktop\\Advent_of_Code\\01_input.txt")

sum = int()
def FuelNeeded (mass):
	fuel = 0

	fuel = math.floor(mass/3)-2
	return fuel

for line in inputfile:
	sum += (FuelNeeded(int(line)))

print(sum)