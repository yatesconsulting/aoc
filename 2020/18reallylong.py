#!/usr/bin/python3

# ~ import itertools
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
	# ~ print ("def getlinesfromfile len(lines)={},len(lines[0])={}".format(len(lines),len(lines[0])))
	return lines

def newmath(eqn, noisy=False):
	ans = ""
	if noisy: print("sub newmath eqn={}".format(eqn))
	if "(" in eqn:
		if noisy: print("found parenthesis")
		p = re.split("[)(]", eqn, 2)
		if p[0] == "":
			if noisy: print("blank on left, newmath(p[1]={}), p[2]={}".format(p[1],p[2]))
			ans = newmath("{} {}".format(newmath(p[1],noisy),p[2]))
		elif p[2] == "":
			if noisy: print("blank on right,newmath(p[0]={}, newmath(p[1]={}))".format(p[0],p[1]))
			ans = newmath("{} {}".format(p[0],newmath(p[1],noisy)))
		else:
			if noisy: print("no blank, p[0]={}, newmath(p[1]={}), p[2]={}".format(p[0],p[1],p[2]))
			ans = newmath("{} {} {}".format(p[0],newmath(p[1],noisy),p[2]))
	p = eqn.split(" ", 2)
	a = len(p)
	if a == 1 and p[0] == "":
		if noisy: print("one space, return empty string")
		ans = ""
	if a == 1 and p[0].isnumeric():  # like 2
		if noisy: print("one number, return it (str)")
		ans = p[0]
	elif a == 2 and p[0].isnumeric(): # like 2 +
		if noisy: print("1 number and one thing, returning those parts,[0]={}, and [1]=".format(p[0],p[1]))
		ans = "{} {}".format(p[0],p[1])
	elif a == 3 and p[0].isnumeric() and p[1] in ('*','+','/','-') and p[2].isnumeric():
		if noisy: print("a==3(={}) and [0](numeric) operator [1](numeric) == {} {} {}".format(a,p[0],p[1],p[2]))
		t0 = int(p[0])
		t2 = int(p[2])
		if p[1] == "*":
			ans = "{}".format(t0 * t2)
		if p[1] == "+":
			ans = "{}".format(t0 + t2)
	elif a == 3 and p[0].isnumeric() and p[1] in ('*','+','/','-'):		
		if noisy: print("a==3(={}) and [0](numeric) operator newmath([1]) == {} {} newmath{}".format(a,p[0],p[1],p[2]))
		t0 = int(p[0])
		
		b0, b1, b2 = p[2].split(" ", 2)
		if b0.isnumeric():
			b0 = int(b0)
			if p[1] == "*":
				ans = newmath("{} {} {}".format(t0 * b0, b1, b2))
			elif p[1] == "+":
				ans = newmath("{} {} {}".format(t0 + b0, b1, b2))
		else:
			print("HEY, I'm stuck here, a=3, p[0-2]={};;;{};;;{};;; and b0-2={};;;{};;;{}".format(p[0],p[1],p[2],b0,b1,b2))
			if p[1] == "*":
				ans = t0 * int(newmath(p[2]))
			if p[1] == "+":
				ans = t0 + int(newmath(p[2]))
		
	if noisy: print("end newmath eqn={}".format(ans))
	return ans

def solvea(lines, noisy=False):
	'''
	order of prescendnce l to r with +-*/ all equal, parens normal
	Evaluate the expression on each line of the homework; what is the sum of the resulting values
	'''
	if noisy: print("def solvea len(lines)={}".format(len(lines)))
	ans = ""
	anstot = 0
	parts = []
	for l in lines:
		ans = ""
		# ~ while (not(ans.isnumeric())):
		ans = newmath(l, noisy)
		if noisy: print("in solvea loop, l, line {} ans(int?) {}".format(l,ans))
		exit()
		anstot += int(ans)
		if noisy: print("l = {}, parts = {}".format(l,parts))
	if noisy: print("returning ones {} * ( threes {})".format(9,12))
	return anstot

	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' 
	'''
	ans = 0
	return ans
	
if __name__ == "__main__":
	lines = getlinesfromfile("18ex1.txt")
	# ~ ansa = solvea([lines[0]], noisy=True)
	# ~ lines = getlinesfromfile("18.txt")
	# ~ ansa = solvea(lines, noisy=True)
	print (newmath("1 + (2 * 3) + (1 + 3) * 2", noisy=True))
	# ~ print("18a: {}".format(ansa))
	# ~ ans = solveb(lines, noisy=True)
	# ~ print("18b: {}".format(ans))
