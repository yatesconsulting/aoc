#!/usr/bin/python3

import re
import numpy as np

def getlinesfromfile(filename):
	lines = []
	infile = open(filename, 'r')
	lines = infile.read().splitlines()
	infile.close()
	return lines

def solvea(lines, finishline=2020, noisy=False):
	'''

	If that was the first time the number has been spoken, 
	the current player says 0.
	Otherwise, the number had been spoken before; the current player 
	announces how many turns apart the number is from when 
	it was previously spoken.

	'''
	n = [int(l) for l in lines[0].split(",")]
	if noisy: print("def solvea with {}".format(n))
	arr = np.array(n)
	# ~ arr1 = np.array([1, 2, 3])
	# ~ arr2 = np.array([4, 5, 6])
	# ~ arr = np.hstack((arr1, arr2))
	# ~ rr = np.hstack((arr, [1,12,23,1,45]))
	# ~ print(arr)
	# ~ #print ((np.where(arr==1)))
	# ~ print ((np.where(arr==1)[0])[-1])
	t = 0
	l = len(arr) - 1 # start process on l + 1, or remove - 1
	while (len(arr) < finishline):
		if arr[l] in arr[:l]:
			d = (np.where(arr==arr[l])[0])[-2]
			t = l - d
			arr = np.hstack((arr, [t]))
		else:
			t = 0
			arr = np.hstack((arr, [0]))
		l += 1
		if noisy: print("{} ".format(l), end="")
		
	return t
	
def solveb(lines, finishline=30000000, noisy=False):
	if noisy: print("def solveb")
	''' 
	X are floating, 0-1 OR
	'''
	n = [int(l) for l in lines[0].split(",")]
	if noisy: print("def solvea with {}".format(n))
	arr = {}
	spoken = 0
	i = 0
	le = len(n)
	
	for i in range(le):
		arr[n[i]] = i
		if noisy: print("loop i={}, val={} ".format(i,n[i]))
		
	for i in range(le, finishline):
		try:
			spoken = n[i-1]
			if noisy: print("a.i={} spoken={}, arr[spoken]={} from n={}".format(i,spoken,"?",n))
			if arr[spoken] < i:
				spoken = i - arr[n[i-1]]
				if noisy: print("b.i={} spoken={}, arr[spoken]={} from nstill={}".format(i,spoken,arr[spoken],n))
			else:
				if noisy: print("c. spoken=0")
				spoken = 0
		except:
			spoken = 0
		finally:
			arr[spoken] = i
			n.append(spoken)
			print ("fin i={}, spoken:{}, arr={}".format(i,spoken,arr))
			# ~ if noisy: print("{} ".format(t), end="")
		
	return spoken
		
if __name__ == "__main__":
	# ~ lines = getlinesfromfile("15.txt")
	# ~ ansa = solvea(lines, noisy=False)
	# ~ print("14a: {}".format(ansa))
	lines = getlinesfromfile("15ex0.txt")
	ansb = solveb(lines, 10, noisy=True)
	print("15b: {}".format(ansb))
