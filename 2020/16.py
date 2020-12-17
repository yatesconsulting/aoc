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

def getgoodnums(line, noisy=False):
	# a-b c-d return a..b,c..d in []
	ans = []
	title = line.split(":")[0]
	
	prog = re.compile(r"([1234567890-]+)")
	pairs = prog.findall(line)
	for p in pairs:
		l,h = p.split("-")
		for t in range(int(l),int(h)+1):
			ans.append(t)
	if noisy: print("getgoodnums sending {}".format(ans))
	return [ans, title]

def solvea(lines, noisy=False):
	'''find groups of numbers with ex: 1-3 or 5-7 means 1-7 valid excluding 4, including 1 and 7
	find lines past "nearby tickets:" that are excluded, and keep track of why (missing #'s)
	return sum of missing numbers
	'''
	goodnums = []
	ck = False
	n = []
	ans = 0
	
	if noisy: print("def solva")
	ans = 0
	for l in lines:
		if noisy: print("i={}".format(l))
		if ck:
			# clean up the goodnums just a little:
			n = l.split(",")
			if noisy: print("imacheckin: {}".format(n))
			for a in n:
				aa = int(a)
				if aa not in goodnums:
					ans += aa
					if noisy: print("found a gap: {}, new ans={}".format(aa,ans))			
		elif "-" in l:
			goodnums += (getgoodnums(l, noisy))[0]
		elif l == "nearby tickets:":
			ck = True
			if noisy: print("Orig size of goodnums = {}".format(len(goodnums)))
			goodnums = set(goodnums)
			if noisy: print("ck now true, using cleaned up goodnums, len={}, val={}".format(len(goodnums),goodnums))
	return ans
	
def whatcodescouldthisbe(a, codes, noisy=False):
	if noisy: print("whatcodescouldthisbe a={}, codes={}".format(a,codes))
	ans = []
	for key,val in codes.items():
		g = True
		if noisy: print("CK code ;;;{};;; of ;;;{};;;".format(key, val))
		for tic in a:
			if noisy: print("checking this num off the tickets for what codes it could fit in: {}".format(tic))
			if tic not in val:
				g = False
				if noisy: print("missed {} in {} -> {} fails".format(tic, val, key))
			else:
				if noisy: print("found {} in {} for code {}".format(tic, val, key))
		if g:
			ans.append(key)
	return ans 
	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' 
	'''
	goodnums = []
	ck = False
	n = []
	ans = 1
	ansc = {}
	codes = {}
	goodtickets = []
	nextlinemyticket = False
	myticket = []
	
	if noisy: print("def solvb")
	for l in lines:
		if noisy: print("i={}".format(l))
		if ck:
			# clean up the goodnums just a little:
			bad = False
			n = [int(a) for a in l.split(",")]
			if noisy: print("imacheckin: {}".format(n))
			for a in n:
				if a not in goodnums:
					# throw out this line
					bad = True
					if noisy: print("Trash line {}".format(l))
			if not bad:
				goodtickets.append(n)
		elif "-" in l:
			ret = (getgoodnums(l, noisy))
			goodnums += ret[0]
			codes[ret[1]] = ret[0]
		elif l == "your ticket:":
			nextlinemyticket = True
		elif nextlinemyticket:
			nextlinemyticket = False
			myticket = [int(a) for a in l.split(",")]
		elif l == "nearby tickets:":
			ck = True
			if noisy: print("Orig size of goodnums = {}".format(len(goodnums)))
			goodnums = set(goodnums)
			if noisy: print("ck now true, using cleaned up goodnums, len={}, val={}".format(len(goodnums),goodnums))
	if noisy: print("ok, got some tickets to look over, mine:\n{} and the good ones:\n{}".format(myticket,goodtickets))
	if noisy: 
		print("and I have some ranges to work with")
		for key,val  in codes.items():
			if noisy: print("key={}, val={}".format(key,val))
	# loop over each element in the ticket, and see which field(s) it must be constrained to
	# once decoded, multiple all values on my ticket that have code starting with departure
	for i in range(len(myticket)):
		a = []
		a.append(myticket[i])
		for b in range(len(goodtickets)):
			if noisy: print("on index {} looking at the ticket {}, so {}".format(i,b,goodtickets[b][i]))
			a.append(goodtickets[b][i])
		# process index i with a having all good numbers
		a = set(a)
		ansc[i] = whatcodescouldthisbe(a, codes, noisy)
		if noisy: print("column {} has ansc = {}".format(i,ansc[i]))
	# maybe just one time through, we're in trouble if not
	for k in sorted(ansc, key=lambda k: len(ansc[k]), reverse=False):
		l =  len(ansc[k])
		if l != 1: print("Dang it!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		if noisy: print ("key={}, val={}".format(k, ansc[k], len(ansc[k])))
		# destroy this option from all others
		for key in ansc:
			if noisy: print("key={}, k={}, ansc[key]={},ansc[k]={}".format(key,k,ansc[key],ansc[k]))
			if key != k and ansc[k][0] in ansc[key]:
				if noisy: print("removing key from list item{} r={}".format(ansc[key],ansc[k][0]))
				ansc[key].remove(ansc[k][0])
		# ok, now we have ansc[col#] = one category, check this one, and 
		if (ansc[k][0])[:9] == "departure":
			ans *= myticket[k]
	return ans
		
if __name__ == "__main__":
	lines = getlinesfromfile("16.txt")
	ansa = solvea(lines, noisy=False)
	print("16a={}".format(ansa))
	lines = getlinesfromfile("16.txt")
	ans = solveb(lines, noisy=False)
	print("16b: {}".format(ans))
