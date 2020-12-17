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
	w = len(lines[0])  - 1
	le = len(lines) -1 
	if noisy: print("w={}, le={}".format(w,le))
	for y in range(le):
		for x in range(w):
			if noisy: print("looking at {},{} and it's value {}".format(x,y,lines[x][y]))
			c = lines[x][y]
			print(prch(c), end="")
		print()
	print()

def linesrecode(lines, noisy=False):
	width = len(lines[0]) - 1
	length = len(lines) - 1
	nlines = []
	ans = []
	l = []
	if noisy: print("wxl = {}x{}".format(width,length))
	for x in range(width):
		xrow = []
		for y in range(length):
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
		if noisy: print("xrow appended by len={}".format(len(xrow)))
		nlines.append(xrow)
	return nlines

def indexck(width, height, x, y, noisy):
	# ~ if noisy: print("sub indexck width={}, height={}, x={}, y={}".format(width,height,x,y))
	if x < 0 or x > width or y < 0 or y > height:
		return False
	return True
	
def emptyfilled(lines, x, y, noisy):
	# return how many seats are filled around me
	ans = 0
	width = len(lines[0]) - 1 # to help with the 0 indexes
	height = len(lines) - 1 # to help with the 0 indexes
	# ~ lines[x-1,y+1]  lines[x,y+1]	lines[x+1,y+1]
	# ~ lines[x-1,y]					lines[x+1,y]
	# ~ lines[x-1,y-1]  lines[x,y-1]	lines[x+1,y-1]
	# ~ if noisy: print("sub emptyfilled x,y {},{} width={}, height={}".format(x,y,width,height))
	if lines[x][y] == "0": return False
	if indexck(width, height, x-1, y+1, noisy): # ul
		ans += (lines[x-1][y+1])
	if indexck(width, height, x, y+1, noisy): # mu  
		ans += (lines[x][y+1])
	if indexck(width, height, x+1, y+1, noisy): # ur
		ans += (lines[x+1][y+1])
	if indexck(width, height, x-1, y, noisy): # lm
		ans += (lines[x-1][y])
	if indexck(width, height, x+1, y, noisy): # rm
		ans += (lines[x+1][y])
	if indexck(width, height, x-1, y-1, noisy): # ll
		ans += (lines[x-1][y-1])
	if indexck(width, height, x, y-1, noisy): # lm
		ans += (lines[x][y-1])
	if indexck(width, height, x+1, y-1, noisy): # lr
		ans += (lines[x+1][y-1])
	return ans

def solvea(lines, noisy=False):
	'''If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change
	'''
	if noisy: print("def solva")
	width = len(lines[0])
	length = len(lines)
	ans = 0
	# ~ nextlines = lines.copy()
	# ~ nextlines = lines[:]
	# ~ nextlines = (lines.copy())[:]
	# ~ nextlines = list(lines)
	# ~ nextlines = (list(lines).copy())[:]
	# ~ nextlines = [[7,8,9],[9,8,7]]
	nextlines = deepcopy(lines)
	
	# ~ unstable = True
	enough = 0
	printlines(lines, noisy)
	# ~ for a in range(10): print("1hmm: - vs {} at {},{}".format(lines[a][0],a,0))
	while (enough < 30):
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
			break
		lines = deepcopy(nextlines)
		printlines(nextlines, noisy)

	for x in range(width):
		ans += sum(nextlines[x])

	return ans
	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' 
	'''
	# break groups into sets that have >= 3 between edges
	ans = 1
	for i in lines:
		pass
	return False
	
if __name__ == "__main__":
	lines = getlinesfromfile("11.txt")
	# ~ print (lines)
	lines = linesrecode(lines, True)
	# ~ print (lines)
	ansa = solvea(lines, noisy=True)
	print("11a == 37 == {}".format(ansa))
	# ~ ans = solveb(lines, noisy=True)
	# ~ print("1lb: {}".format(ans))
