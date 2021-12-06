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

def howmanyblack(loc, noisy=False):
	ans = 0
	for a in loc.values():
		ans += (a==1) # add up trues for tot?
	return ans

def newxy(a, x, y, noisy=False):
	if a == "nw":
		x -= 1
		y += 1
	elif a == "ne":
		y += 1
	elif a == "sw":
		y -= 1
	elif a == "se":
		x += 1
		y -= 1
	elif a == "w":
		x -= 1
	elif a == "e":
		x += 1
	else:
		print ("WHATT?? {}".format(a))
	return (x,y)

def solvea(lines, noisy=False):
	'''white side up to start, directions e,w,nw,ne,se,sw all together
	how many tiles are left with the black side up?
	'''
	if noisy: print("def solvea")
	x = 0
	y = 0
	loc = {}
	
	ans = 0
	for l in lines:
		# start each line at 0,0
		x,y = 0,0
		# and all tiles white
		# ~ loc.clear()
		# and move the series, in one or 2 letter sets
		m = re.findall("nw|ne|sw|se|w|e",l)
		# each line defines ONE tile to flip, but they may be flipped multiple times in all lines
		for a in m:
			if noisy: print("on line {} a={}".format(l,a))
			x,y = newxy(a, x, y)
			# ~ if a == "nw":
				# ~ x -= 1
				# ~ y += 1
			# ~ elif a == "ne":
				# ~ y += 1
			# ~ elif a == "sw":
				# ~ y -= 1
			# ~ elif a == "se":
				# ~ x += 1
				# ~ y -= 1
			# ~ elif a == "w":
				# ~ x -= 1
			# ~ elif a == "e":
				# ~ x += 1
			# ~ else:
				# ~ print ("WHATT?? {}".format(a))
		try:
			loc["{},{}".format(x,y)] *= -1 # -1 == white, *= -1 == toggle
		except:
			loc["{},{}".format(x,y)] = 1 # 1 == black
	ans = howmanyblack(loc) 
	return (ans,loc)

def findmyblackneighbors(locs, me, noisy=False):
	x,y = [int(a) for a in me.split(",")]
	xt,yt = 0,0
	n = []
	b = 0
	w = 0
	for d in ['nw','ne','e','se','sw','w']:
		xt,yt = newxy(d, x, y, noisy)
		n.append("{},{}".format(xt,yt))
	for a in n:
		if a in locs.keys() and locs[a] == 1:
			b += 1
	return b
	
def flipwhites(locs, noisy=False):
	# white tile with exactly 2 black neighbors flips to black
	flipper = []
	for a in locs.keys():
		if locs[a] == -1:
			b = findmyblackneighbors(locs, a, noisy)
			if b == 2:
				flipper.append(a)	
	return flipper

def flipblacks(locs, noisy=False):
	# black tile 0 or > 2 flips to white
	flipper = []
	for a in locs.keys():
		if locs[a] == 1:
			b = findmyblackneighbors(locs, a, noisy)
			if b>2 or b == 0:
				flipper.append(a)	
	return flipper

# ~ def findnewblacks(locs, noisy=False):
	# ~ # new black tile exactly 2 black neighbors, no key
	# ~ x = []
	# ~ y = []
	# ~ a = ""
	# ~ xy = list(locs.keys())
	# ~ x = [int(a.split(",")[0]) for a in xy]
	# ~ y = [int(a.split(",")[1]) for a in xy]
	# ~ for a in range(min(x)-1,max(x)+1):
		# ~ for b in range(min(y)-1,max(y)+1):
			# ~ k = "{},{}".format(a,b)
			# ~ if k not in xy:
				# ~ locs[k] = -1
	# ~ return flipwhites(locs, noisy)

def expandboardalittle(locs, noisy=False):
	x = []
	y = []
	a = ""
	xy = list(locs.keys())
	x = [int(a.split(",")[0]) for a in xy]
	y = [int(a.split(",")[1]) for a in xy]
	xmin = min(x) - 2
	xmax = max(x) + 2
	ymin = min(y) - 2
	ymax = max(y) + 2
	# ~ if noisy: print("xy={}".format(xy))
	# ~ if noisy: print("xmin,xmax={},{} from x={}".format(xmin,xmax,x))
	# ~ if noisy: print("ymin,ymax,xmax={},{} from y={}".format(ymin,ymax,y))
	for a in range(xmin,xmax):
		for b in range(ymin,ymax):
			k = "{},{}".format(a,b)
			if k not in xy:
				locs[k] = -1
	return locs

def visualizeboard(locs, noisy=False):
	x = []
	y = []
	a = ""
	k = ""
	xy = list(locs.keys())
	x = [int(a.split(",")[0]) for a in xy]
	y = [int(a.split(",")[1]) for a in xy]
	for a in range(min(x)-1,max(x)+1):
		for b in range(min(y)-1,max(y)+1):
			k = "{},{}".format(a,b)
			if k not in xy:
				print("- ", end="")
			elif locs[k] == 1:
				print("B ", end = "")
			elif locs[k] == -1:
				print("W ", end = "")
			else:
				print ("! ",end = "")
		if a == 0:
			print("<-- x=0",end="")
		if a%2:
			print("\n ",end="");
		else:
			print();

def solveb(locs, noisy=False):
	if noisy: print("def solveb")
	''' life with black tile 0 or > 2 flips to white
	white tile with exactly 2 flips to black
	each generation, start with a as input
	locs are indexed by x,y and -1=white, 1 = black
	after 100 days, hwo many, ex1= 2208
	'''
	ans = 0
	whitestoflip = []
	blackstoflip = []
	for i in range(100):
		# ~ if noisy: visualizeboard(locs, noisy)
		locs = expandboardalittle(locs, noisy)
		blackstoflip = flipblacks(locs, noisy)
		whitestoflip = flipwhites(locs, noisy)
		# ~ newblacks = findnewblacks(locs, noisy)
		for ii in whitestoflip:
			locs[ii] = 1
		for ii in blackstoflip:
			locs[ii] = -1
		if noisy: print("After day {}, we have {} blacks".format(i+1,howmanyblack(locs)))
	return ans
	
if __name__ == "__main__":
	lines = getlinesfromfile("24.txt") # 10
	ansa,loc = solvea(lines, noisy=False)
	print("24a: {}".format(ansa))
	# ~ lines = getlinesfromfile("24ex1.txt") # 10
	ans = solveb(loc, noisy=False)
	print("24b: {}".format(ans))
	
