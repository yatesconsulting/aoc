#!/usr/bin/python3

# ~ import types
from copy import copy, deepcopy

def getlinesfromfile(filename):
	lines = []
	
	infile = open(filename, 'r')
	# ~ lines = [int(line) for line in infile.readlines()] # single int on each line
	# ~ lines = infile.readlines() # leave on the newlines
	# ~ lines = infile.read().splitlines()
	# each element on each line in the 2d array lists
	for l in infile.read().splitlines():
		lines.append(list(l)) # this does reverse [x][y] to [y][x]
	infile.close()
	
	# ~ print ("len(lines)={},len(lines[0])={}".format(len(lines),len(lines[0])))
	return lines

def prch(c):
	if type(c) == bool and c:
		return "#"
	elif type(c) == bool and not(c):
		return "L"
	elif c == "L" or c == "#":
		return c
	else:
		return "."
	
def printlines(lines, noisy=False):
	d1 = len(lines[0])  
	d2 = len(lines)
	if noisy: print("d1=len(lines[0]={}, d2=len(lines)={}".format(d1,d2))
	for y in range(d1):
		for x in range(d2):
			# ~ if noisy: print("looking at {},{} and it's value {} from d2,d1, len(lines),len(lines[0])={},{}".format(x,y,lines[x][y],d2,d1))
			c = lines[x][y]
			print(prch(c), end="")
		print()
	print()

def linesrecode(lines, noisy=False):
	if noisy: print("def linerecode, len(lines)={} len(lines[0])={}".format(len(lines),len(lines[0])))
	d1 = len(lines[0]) # width
	d2 = len(lines)	# length
	nlines = []
	ans = []
	l = []
	for x in range(d1):
		xrow = []
		for y in range(d2):
			# ~ if noisy: print("a = lines[y][x] = lines[{}][{}] == {}".format(y,x,lines[y][x]))
			a = lines[y][x] # this is the only place indexes are y, then x
			if a == "#":
				a = True
			elif a == "L":
				a = False
			elif a == ".":
				a = 0
			else:
				print("Error")
			xrow.append(a)
		# ~ if noisy: print("xrow appended by len={}".format(len(xrow)))
		nlines.append(xrow)
	if noisy: print("def linerecode done, len(nlines)={} len(nlines[0])={}".format(len(nlines),len(nlines[0])))
	return nlines

def indexck(width, height, x, y, noisy):
	if noisy: print("sub indexck width={}, height={}, x={}, y={}".format(width,height,x,y))
	if x < 0 or x > width or y < 0 or y > height:
		return False
	return True
	
def emptyfilled(lines, x, y, noisy):
	# return how many seats are filled around me
	ans = 0
	d1index = len(lines[0]) - 1  # to help with the 0 indexes without using range
	d2index = len(lines) - 1  # to help with the 0 indexes
	# ~ lines[x-1,y+1]  lines[x,y+1]	lines[x+1,y+1]
	# ~ lines[x-1,y]					lines[x+1,y]
	# ~ lines[x-1,y-1]  lines[x,y-1]	lines[x+1,y-1]
	# ~ if noisy: print("sub emptyfilled x,y {},{} d2index={}, d1index={}".format(x,y,d2index,d1index))
	if lines[x][y] == "0": return False
	if indexck(d2index, d1index, x-1, y+1, noisy): # ul
		ans += (lines[x-1][y+1])
	if indexck(d2index, d1index, x, y+1, noisy): # mu  
		ans += (lines[x][y+1])
	if indexck(d2index, d1index, x+1, y+1, noisy): # ur
		ans += (lines[x+1][y+1])
	if indexck(d2index, d1index, x-1, y, noisy): # lm
		ans += (lines[x-1][y])
	if indexck(d2index, d1index, x+1, y, noisy): # rm
		ans += (lines[x+1][y])
	if indexck(d2index, d1index, x-1, y-1, noisy): # ll
		ans += (lines[x-1][y-1])
	if indexck(d2index, d1index, x, y-1, noisy): # lm
		ans += (lines[x][y-1])
	if indexck(d2index, d1index, x+1, y-1, noisy): # lr
		ans += (lines[x+1][y-1])
	return ans

def ckspot(d2index, d1index, x2, y2, noisy=False):
	''' if found and should stop, return true and either way return a safe ans+= val
	'''
	ans = 0
	foundsomething = False
	if indexck(d2index, d1index, x2, y2, noisy):
		t = prch(lines[x2][y2])
		if t in ("L","#"):
			ans += lines[x2][y2]
			foundsomething = True
	return (foundsomething, ans)

def eachdirection(lines, x, y, noisy):
	''' return how many of the first kind of seats you can see (0-8) in 
	each of the 8 directions, first type shadows others
	
0=  . = floor
True = # = taken
False = L = available

	'''
	ans = 0
	d1index = len(lines[0]) - 1  # to help with the 0 indexes without using range
	d2index = len(lines) - 1  # to help with the 0 indexes
	# ~ lines[x-1,y+1]  lines[x,y+1]	lines[x+1,y+1]
	# ~ lines[x-1,y]					lines[x+1,y]
	# ~ lines[x-1,y-1]  lines[x,y-1]	lines[x+1,y-1]
	# ~ if noisy: print("sub emptyfilled x,y {},{} d2index={}, d1index={}".format(x,y,d2index,d1index))
	if prch(lines[x][y]) == ".": return False
	tx = x
	ty = y
	r = 0
	d1 = 0 # ne
	d2 = 0 # e
	d3 = 0 # se
	d4 = 0 # nw
	d5 = 0 # w
	d6 = 0 # sw
	d7 = 0 # n
	d8 = 0 # s
	managable = False
	x2 = x
	y2 = y
	while (r < 20000 and not (d1 and d2 and d3 and d4 and d5 and d6 and d7 and d8)):
		r += 1
		if not d1:
			x2 = x + r
			y2 = y + r
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d1 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d2:
			x2 = x + r
			y2 = y 
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d2 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d3:
			x2 = x + r
			y2 = y - r
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d3 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d4:
			x2 = x - r
			y2 = y + r
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d4 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d5:
			x2 = x - r
			y2 = y
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d5 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d6:
			x2 = x - r
			y2 = y - r
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d6 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d7:
			x2 = x
			y2 = y + r
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d7 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
		if not d8:
			x2 = x
			y2 = y - r 
			a,b = ckspot(d2index, d1index, x2, y2)
			if a:
				d8 = r
				ans += b
				if noisy: print("d1 found a {} at r={}".format(b,r))
	if noisy: print("For {},{}, I return {} r's for d's were: {},{},{},{},{},{},{},{}".format(x,y,ans,d1,d2,d3,d4,d5,d6,d7,d8))
	return ans
	
def solvea(lines, noisy=False):
	'''If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change
	'''
	if noisy: print("def solva")
	length = len(lines[0])
	width = len(lines)
	ans = 0
	# ~ nextlines = lines.copy()
	# ~ nextlines = lines[:]
	# ~ nextlines = (lines.copy())[:]
	# ~ nextlines = list(lines)
	# ~ nextlines = (list(lines).copy())[:]
	nextlines = deepcopy(lines)
	enough = 0

	if noisy: printlines(lines, noisy)
	# ~ for a in range(10): print("1hmm: - vs {} at {},{}".format(lines[a][0],a,0))
	while (enough < 30 ):
		if noisy: print("in the while loop nextlines != lines")			
		for y in range(length): # range(length):
			for x in range(width): # range (width)
				c = lines[x][y]
				fc = emptyfilled(lines, x, y, noisy)
				# ~ if noisy: print("x,y={},{}, c={} type={} prch(c)={} for  fc={}\nlines={}\nnextlines={}".format(x,y,c,type(c),prch(c),fc, lines, nextlines))
				if type(c) == bool and c == False:
					# ~ if noisy: print("FalseCheck: x,y = {},{} = {}, about to flip to True".format(x,y,c))
					if fc == 0:
						nextlines[x][y] = True
				elif type(c) == bool and c == True :
					# ~ if noisy: print("TrueCheck: x,y = {},{} = {} about to flip to False".format(x,y,c))
					if fc >= 4:
						nextlines[x][y] = False
		enough += 1
		if lines == nextlines:
			print("found lines==nextlines")
			break
		lines = deepcopy(nextlines)
		if noisy: printlines(nextlines, noisy)

	for x in range(width):
		ans += sum(nextlines[x])

	return ans
	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' it now takes five or more visible occupied seats for an 
	occupied seat to become empty (rather than four or more from the 
	previous rules). The other rules still apply: empty seats that see 
	no occupied seats become occupied, seats matching no rule don't 
	change, and floor never changes.
	'''
	# break groups into sets that have >= 3 between edges
	length = len(lines[0])
	width = len(lines)
	ans = 0
	# ~ nextlines = lines.copy()
	# ~ nextlines = lines[:]
	# ~ nextlines = (lines.copy())[:]
	# ~ nextlines = list(lines)
	# ~ nextlines = (list(lines).copy())[:]
	nextlines = deepcopy(lines)
	enough = 0

	if noisy: printlines(lines, noisy)
	# ~ for a in range(10): print("1hmm: - vs {} at {},{}".format(lines[a][0],a,0))
	while (enough < 10 ):
		if noisy: print("in the while loop nextlines != lines")			
		for y in range(length): # range(length):
			for x in range(width): # range (width)
				c = lines[x][y]
				# ~ fc = emptyfilled(lines, x, y, noisy)
				fc = eachdirection(lines, x, y, noisy)
				# ~ if noisy: print("x,y={},{}, c={} type={} prch(c)={} for  fc={}\nlines={}\nnextlines={}".format(x,y,c,type(c),prch(c),fc, lines, nextlines))
				if type(c) == bool and c == False:
					if fc == 0:
						if noisy: print("FalseCheck: x,y = {},{} = {}, about to flip to True".format(x,y,c))
						nextlines[x][y] = True
					else:
						if noisy: print("FalseCheck: x,y = {},{} = {}, Nothing done, fc={}".format(x,y,c,fc))
				elif type(c) == bool and c == True :
					if fc >= 5:
						if noisy: print("TrueCheck: x,y = {},{} = {} about to flip to False, fc={}".format(x,y,c,fc))
						nextlines[x][y] = False
					else:
						if noisy: print("TrueCheck: x,y = {},{} = {}, no flip, fc={}".format(x,y,c,fc))
		enough += 1
		if lines == nextlines:
			if noisy: print("found lines==nextlines")
			break
		lines = deepcopy(nextlines)
		if noisy: printlines(nextlines, noisy)

	for x in range(width):
		ans += sum(nextlines[x])

	return ans
	
	
if __name__ == "__main__":
	lines = getlinesfromfile("11ex1.txt")
	lines = linesrecode(lines, False)
	# ~ ansa = solvea(lines, noisy=False)
	# ~ print("11a == {}".format(ansa)) # 1530 too low
	# ~ lines = getlinesfromfile("11ex1.txt")
	ans = solveb(lines, noisy=True)
	print("1lb: {}".format(ans))
