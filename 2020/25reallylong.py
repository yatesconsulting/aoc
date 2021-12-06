#!/usr/bin/python3

import itertools
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
	
	# ~ print ("len(lines)={},len(lines[0])={}".format(len(lines),len(lines[0])))
	return lines

def solvea(lines, noisy=False):
	'''
	'''
	if noisy: print("def solvea")
	c1 = int(lines[0])
	c2 = int(lines[1])
	x = 1
	y = 1
	f = 7
	'''
	The handshake used by the card and the door involves an operation 
	that transforms a subject number. To transform a subject number,
	start with the value 1. Then, a number of times called the loop 
	size, perform the following steps:

	Set the value to itself multiplied by the subject number.
	Set the value to the remainder after dividing the value by 20201227.
	'''

	# ~ 1526110
	# ~ 20175123	
	
	
	while (f^x%20201227 != c1):
		x += 1
	while (f^y%20201227 != c2):
		y += 1
	# or f^y%20201227^x%20201227 != f^x%20201227^y%20201227):
	#	i = 0
			
	if noisy: print("{}^{}%20201227={}=={}; {}^{}%20..={}=={} c2^x%20201227={} =?= {} = c1^y%20201227".format(f,x,f^x%20201227,c1,f,y,f^y%20201227,c2,c2^x%20201227,c1^y%20201227))
	# c1 = (f^x)%20201227
	# c2 = (f^y)%20201227
	# ans = c2^x%20201227 == c1^y%20201227
	return c2^x%20201227 # not 19173450
	# ~ 7^1526105%20201227=1526110==1526110; 7^20175124%20..=20175123==20175123 c2^x%20201227=19173450 =?= 19173450 = c1^y%20201227
	# ~ 25a: 19173450
	
	
def solveb(locs, noisy=False):
	if noisy: print("def solveb")
	''' 
	'''
	ans = 0
	return ans
	
if __name__ == "__main__":
	lines = getlinesfromfile("25.txt") # 
	ansa = solvea(lines, noisy=True)
	print("25a: {}".format(ansa))
	# ~ lines = getlinesfromfile("24ex1.txt") # 10
	# ~ ans = solveb(loc, noisy=False)
	# ~ print("25b: {}".format(ans))
	
