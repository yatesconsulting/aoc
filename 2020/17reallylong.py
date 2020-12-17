#!/usr/bin/python3

# ~ import types
import re

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
	return lines

def solvea(lines, noisy=False):
	''' life in 3d cube
	
    If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
How many cubes are left in the active state after the sixth cycle?
	'''
	if noisy: print("def solva")

	ans = 0
	for l in lines:
		if noisy: print("l={}".format(l))
	return ans
	
	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' 
	'''
	ans = 1
	for l in lines:
		if noisy: print("l={}".format(l))
	return ans
		
if __name__ == "__main__":
	lines = getlinesfromfile("17ex1.txt")
	ansa = solvea(lines, noisy=True)
	print("17a={}".format(ansa)) # 112 is ex1
	
	# ~ lines = getlinesfromfile("17ex2.txt")
	# ~ ans = solveb(lines, noisy=True)
	# ~ print("17b: {}".format(ans))
