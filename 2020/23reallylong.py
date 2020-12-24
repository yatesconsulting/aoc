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
	
def printdeck(deck,noisy=False):
	print("pretty={}".format(".".join([str(d) for d in deck])))
	
def newl(deck, noisy=False):
	if noisy: print ("sub newl,  len(deck) = {}".format(len(deck)))
	if noisy: printdeck(deck, noisy)
	# ~ ans = ""
	ar = list(deck) # + [""]
	one = ar[0:1]
	pulled = ar[1:4]
	dest = one[0] - 1
	if dest == 0:
		dest = max(ar[4:]) 
	while (dest in pulled):
		if noisy: print ("I see {} in pulled".format(dest))
		dest -= 1
		if dest == 0:
			dest = int(max(ar[4:]))
	droppt = ar.index(dest)
	if noisy: print("one={} pulled={} ar[4:5]={} ar[5:droppt+1]={} ar[droppt+1:]={} dest={} droppt={}".format(one,pulled,ar[4:5],ar[5:droppt+1],ar[droppt+1:],dest,droppt)) # rotate array and replace parts
	
	newar = ar[4:5] + ar[5:droppt+1] + pulled + ar[droppt+1:] + one # rotate array and replace parts
	# ~ ans = "".join(newar)
	# ~ if noisy: print("after move, deck: {}".format(ans))
	return newar

def solvea(lines, moves = 10, noisy=False):
	'''run the numbers
	line = 32415
	start at 3, pick up 3 after, 241
	then find next number < 3, rolling around if missing, not counting cups you just picked up
	move 3 cups after that cup
	move rt 1 (4 if you handn't moved 3 cups)
	move is complete
	after X number of these, then shift list until 1 is at start, and return rest of string (len-1)
	'''
	ans = 0
	lines = list(lines)
	lines = [int(line) for line in lines]
	for i in range(moves):
		if noisy: print("i={}".format(i))
		lines = newl(lines, noisy)
	
	start = lines.index(1)
	print ("start={} was {}".format(start, lines))
	ans = (lines[start:]+lines[:start])[1:]
	return ans
	
def solveb(lines, moves = 10, noisy=False):
	'''run the numbers
	line = 32415
	start at 3, pick up 3 after, 241
	then find next number < 3, rolling around if missing, not counting cups you just picked up
	move 3 cups after that cup
	move rt 1 (4 if you handn't moved 3 cups)
	move is complete
	after X number of these, then shift list until 1 is at start, and return rest of string (len-1)
	'''
	if noisy: print("def solveb")
	ans = 0
	lines = list(lines)
	lines = [int(line) for line in lines]
	st = max(lines)
	for i in range(st+1, 1000001):
		lines.append(i)
	for i in range(moves):
		if noisy: print("i={}".format(i))
		lines = newl(lines, noisy)
	start = lines.index(1)
	ans = ((lines[start:]+lines[:start])[1:])[0:2]
	print ("ans doesn't ={}, but does={}".format(ans, ans[0]*ans[1]))
	# ~ ans = "".join(newar)
	# ~ if noisy: print("after move, deck: {}".format(ans))
	return ans[0]*ans[1]

if __name__ == "__main__":
	# ~ lines = getlinesfromfile("23ex1.txt")
	# ~ lines = "389125467" # example
	# ~ ansa = solvea(lines, moves =10, noisy=True)
	# ~ print("22a: {}".format(ansa))

	# ~ lines = "739862541" # real
	# ~ ansa = solvea(lines, moves=100	, noisy=True)
	# ~ print("22a: {}".format(ansa))

	# ~ lines = "389125467" # example
	# ~ ans = solveb(lines, 10000000, noisy=False
	# ~ # 934001 * 159792 = 149245887792
	# ~ print("23b: {}".format(ans))

	lines = "739862541" # real
	ans = solveb(lines, 10000000, noisy=False)
	print("23b: {}".format(ans))
	
