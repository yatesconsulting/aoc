#!/usr/bin/python3

import re

def getlinesfromfile(filename):
	lines = []
	infile = open(filename, 'r')
	lines = infile.read().splitlines()
	infile.close()
	return lines

def solvea(lines, noisy=False):
	'''
mask=1X0... for 32 bits, 1/0 overwrites, X does nothing
mem[#] = ## assigns position # value ## masked with mask
ans = sum of all positions, all start at 0
	'''
	if noisy: print("def solvea")
	mem = {}
	ans = 0
	for li in lines:
		# ~ if noisy: print("li = {}, split={}".format(li,li.split()))
		p1, val = li.split(" = ")
		if p1 == "mask":
			mask = val
			ormask = int(mask.replace("X","0"), 2)
			andmask = int(mask.replace("X", "1"), 2)
			if noisy: print("new mask: {}\n, and	 {}\nor		{}".format(mask,andmask,ormask))
		else:
			# mask and insert mem[62998] = 9708340
			# mem[33440] = 124867031
			# mem[6869] = 81126
			index = int(re.split("[\[\]]", p1)[1])
			masked = int(val) & andmask | ormask
			if noisy: print("mem[{}] = \n{} unmasked, masked by AND \n{} and then masked by OR\n{} to become final answer: \n{} masked".format(index,val,andmask, ormask,masked))
			mem[index] = masked
	for a in mem.values():
		# ~ print ("val={}".format(a))
		ans += a
	return ans
	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' 
	X are floating, 0-1 OR
	'''
	mem = {}
	ans = 0
	masklist = []
	for li in lines:
		# ~ if noisy: print("li = {}, split={}".format(li,li.split()))
		p1, val = li.split(" = ")
		if p1 == "mask":
			mask = val
			ormask = int(mask.replace("X","0"), 2)
			masklist = []
			masklist = ([pos for pos, char in enumerate(mask) if char == "X"])
			if noisy: print("new mask: {} or {} and masklist {}".format(mask,ormask,masklist))
		else:
			# mask and insert mem[62998] = 9708340
			# mem[33440] = 124867031
			# mem[6869] = 81126
			index = int(re.split("[\[\]]", p1)[1])
			masked = int(val) | ormask
			# ~ if noisy: print("mem[{}] = \n{} unmasked, masked by {} to become final answer: \n{} masked".format(index,val,andmask, ormask,masked))
			mem[index] = masked
			for i in masklist:
				print("need to float {} with character {} of {}".format(masked,i,mask))
	for a in mem.values():
		# ~ print ("val={}".format(a))
		ans += a
	return ans
		
if __name__ == "__main__":
	# ~ lines = getlinesfromfile("14.txt")
	# ~ ansa = solvea(lines, noisy=False)
	# ~ print("14a: {}".format(ansa))
	lines = getlinesfromfile("14ex2.txt")
	ansb = solveb(lines, noisy=False)
	print("14b: {}".format(ansb))
