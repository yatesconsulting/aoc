#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def smallestside(l, w, h):
	return sorted((l*w, w*h, h*l))[0]

def solvea(input):
	''' north (^), south (v), east (>), or west (<)
	return number of houses with 1 or more gifts
	^ = 2 as the starting house always gets one
	'''
	x = 0
	y = 0
	ans = {'0,0' : 1}
	for a in input:
		for b in a:
			if b == ">" : x += 1
			if b == "<" : x -= 1
			if b == "^" : y -= 1
			if b == "v" : y += 1
			ans["{},{}".format(x,y)] = 1
	# ~ for a in ans.keys():
		# ~ print("found a key in ans.keys of {}".format(a))
	return len(ans.keys())
	
def solveb(input):
	''' Robo Santa takes every other one of the commands, now how many
	houses are covered?
	'''
	i = 0
	x = [0,0]
	y = [0,0]
	ans = {'0,0' : 1}
	for a in input:
		for b in a:
			if b == ">" : x[i] += 1
			elif b == "<" : x[i] -= 1
			elif b == "^" : y[i] -= 1
			elif b == "v" : y[i] += 1
			ans["{},{}".format(x[i], y[i])] = 1
			i = 0 if i else 1;
	# ~ for a in ans.keys():
		# ~ print("found a key in ans.keys of {}".format(a))
	return len(ans.keys())

if __name__ == "__main__":
    # lines.sort() # sorts in place, no return value
    lines = getlinesfromfile("3.txt")
    print("3a: Found: {}".format(solvea(lines)))
    print ("3b: Found: {}".format(solveb(lines)))
