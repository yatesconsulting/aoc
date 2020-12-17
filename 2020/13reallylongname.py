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
	return lines

	

def solvea(lines, noisy=False):
	'''find bus number * minutes wait
	'''
	ans = {}
	tm = int(lines[0])
	busses = lines[1].split(",")
	for b in busses:
		if b != "x":
			b = int(b)
			ans[b] = (int(tm/b)+1)*b
	print(tm, ans)
	i = (min(ans, key=ans.get))
	print (i)
	return i * (ans[i] - tm)

def goodset(n, busses, noisy=False):
	a = n * busses[0]
	ans = True
	if noisy: print("def goodset n={}, a={}".format(n,a))
	for i in range(len(busses)):
		if noisy: print("i={},len(busses)={}".format(i,len(busses)))
		if busses[i] > 0:
			if noisy: print("Real bus: {} with index {}".format(busses[i],i))
			c = (a + i) % busses[i]
			if noisy: print("\n1if ((a + i) % busses[i]) > 0:\n2if (({} + {}) % {} > 0: = {}".format(a,i,busses[i],c))
			if c > 0:
				# ~ print("Setting answer to FALSE")
				ans = False
	return ans

def solveb(lines, ans, n=1, noisy=False):
	''' find some bus schedule start time t
	'''
	lastline = len(lines) - 1
	busses = lines[lastline].replace("x","0").split(",")
	busses = [int(b) for b in busses]
	if noisy: print("def solveb busses={}".format(busses))
	while (1): # n <= ans):
		if goodset(n, busses, noisy):
			print("found it, n={}".format(n))
			return n * busses[0]
		n += 1
		if not(n%1000000): print(n)
		
def solvebcos(lines, noisy=False):
	''' find some bus schedule start time t
	'''
	lastline = len(lines) - 1
	busses = lines[lastline].replace("x","0").split(",")
	busses = [int(b) for b in busses]
	if noisy: print("def solveb busses={}".format(busses))
	# find the 1st positive intersection of the cos(
	
if __name__ == "__main__":
	# ~ lines = getlinesfromfile("13.txt")
	# ~ ansa = solvea(lines, noisy=False)
	# ~ print("13a: {}".format(ansa))
	# ~ lines = getlinesfromfile("13ex3.txt")
	# ~ print (lines)
	# ex2: 3417 is correct
	# real answer, 202110726 is too low
	# ex3: 754018
	lines = []
	# ~ lines.append("67,7,59,61") ; ans = 754018/67 # = 11254 # first occurs at timestamp 754018.
	# ~ lines.append("67,x,7,59,61") ; ans = 779210 / 67# first occurs at timestamp 779210.
	# ~ lines.append("67,7,x,59,61"); ans =  1261476 / 67 # first occurs at timestamp 1261476.
	# ~ lines.append("1789,37,47,1889") # first occurs at timestamp 1202161486.
	lines = getlinesfromfile("13.txt") # now this has an extra line
	# ~ startn = 1202161486 / 67 - 1 # 11254
	# ~ startn = ans - 1
	startn = 1
	startn = int(100000000000000 / int(lines[0].split(",")[0])) 
	ans = 9999999999999999999999
	ans = solveb(lines, ans, startn, noisy=False)
	# ~ ans = solvebcos(lines, noisy=False)
	print("13b: {}".format(ans))
	# 99999999109336 is too low
	# 99999999109336

