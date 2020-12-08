#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def solvea(input):
	''' ( = up one, ) = down one, start at 0
	'''
	floor = 0;
	step = 0;
	for a in input:
		for b in a:
			if b == "(": 
				floor += 1
				step += 1
			if b == ")":
				floor -= 1;
				step += 1
			if floor == -1:
				print("hit the basement on step: {}".format(step))
	return floor;


if __name__ == "__main__":
    # lines.sort() # sorts in place, no return value
    lines = getlinesfromfile("1.txt")
    print("1a: Found: {}".format(solvea(lines)))
    #print ("1b: Found: {}".format(sumsof2numberslessthan2020(lines)))
