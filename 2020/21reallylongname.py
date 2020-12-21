#!/usr/bin/python3

import itertools

def getlinesfromfile(filename):
	lines = []
	
	infile = open(filename, 'r')
	# ~ lines = [int(line) for line in infile.readlines()] # single int on each line
	# ~ lines = infile.readlines() # leave on the newlines
	lines = infile.read().splitlines()
	# each element on each line in the 2d array lists
	# ~ for l in infile.read().splitlines():
		# ~ lines.append(list(l)) # this does reverse [x][y] to [y][x]
	# ~ infile.close()
	
	# ~ print ("len(lines)={},len(lines[0])={}".format(len(lines),len(lines[0])))
	return lines

def solvea(lines, noisy=False):
	'''
	'''
	if noisy: print("sub solvea")
	ans = 0
	for l in lines:
		if noisy: print("l={}".format(l))
	return ans

	
def solveb(lines, noisy=False):
	''' 
	'''
	if noisy: print("def solveb")
	ans = 0
	if noisy: print("slines = {}".format(slines))
	return ans
	
if __name__ == "__main__":
	lines = getlinesfromfile("21ex1.txt")
	ansa = solvea(lines, noisy=True)
	print("21a: {}".format(ansa))
	# ~ ans = solveb(lines, noisy=False)
	# ~ print("21b: {}".format(ans))
