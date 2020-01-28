from time import time
start_time = time()

data = list(map(int, open("16_Advent_of_Code.txt").read()))

def part1(inp):

	base = (0,1,0,-1)
	for _ in range(100):
		for h in range(len(inp)):
			b = 0
			f = 0
			temp = 0
			for i in range(len(inp)):
				if i == 0:
					f += 1
				if f % (h+1) == 0:
					f = 0
					if b+1 == len(base):
						b = 0
					else:
						b +=1 
				f += 1
				temp += inp[i]*base[b]
			inp[h] = abs(temp)%10
	
	return(''.join(str(x) for x in inp[:8]))		
def part2(inp):

	realsignal = (inp*10000)[int(''.join(str(x) for x in inp[:7])):]
	for _ in range(100):
		previous = 0
		for x in range(len(realsignal)-1,-1,-1):
			realsignal[x] = previous = abs(previous + realsignal[x]) % 10
	return(''.join(str(x) for x in realsignal[:8]))		



assert part1(list(map(int,"80871224585914546619083218645595"))) == "24176176"
assert part1(list(map(int,"19617804207202209144916044189917"))) == "73745418"
assert part1(list(map(int,"69317163492948606335995924319873"))) == "52432133"

assert part2(list(map(int,"03036732577212944063491565474664"))) == "84462026"
assert part2(list(map(int,"02935109699940807407585447034323"))) == "78725270"
assert part2(list(map(int,"03081770884921959731165446850517"))) == "53553731"

print("Assertion complete after %s seconds" % (time()-start_time))



print("Part 1: {0}, Part 2: {1}".format(part1(data[:]),part2(data[:])))



print("--- {0} seconds ---".format(time()-start_time))
