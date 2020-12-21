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
	
def findlrs(tiles, noisy=False):
	if noisy: print("def findlrs")
	lrans = [] # left to right
	udans = [] # top to bottom
	k =  list(tiles.keys())
	ni = len(k)
	if noisy: print("index ni={}, k={}".format(ni,k))
	
	for i in range(ni):
		for j in range(i+1,ni):
			if noisy: print("i={}, j={}".format(i,j))
			if noisy: print("ck tile {} against tile {}".format(k[i],k[j]), end="")
			if (k[i])[:-1] == (k[j])[:-1]:
				if noisy: print(" Same tile, skip {} == {}".format((k[i])[:-1],(k[j])[:-1]))
				continue
			# check tile i against tile j+1 left-right -> t2-t1
			if noisy: print("Checking position 1, {} =?= {}".format(tiles[k[i]][0],tiles[k[j]][1]))
			if tiles[k[i]][0] == tiles[k[j]][1]:
				lrans.append("{}{}".format(k[j],k[i]))
				if noisy: print(" YES Ladding {}{} from val:{}".format(k[j],k[i],tiles[k[i]][0]),end = "")
			if noisy: print("Checking position 2, {} =?= {}".format(tiles[k[i]][1],tiles[k[j]][0]))
			if tiles[k[i]][1] == tiles[k[j]][1]:
				lrans.append("{}{}".format(k[i],k[j]))
				if noisy: print(" YES Ladding {}{} from val:{}".format(k[i],k[j],tiles[k[i]][1]),end = "")
			if noisy: print("Checking position 3, {} =?= {}".format(tiles[k[i]][2],tiles[k[j]][3]))
			if tiles[k[i]][2] == tiles[k[j]][3]:
				udans.append("{}{}".format(k[j],k[i]))
				if noisy: print(" YES Uadding {}{} from val:{}".format(k[j],k[i],tiles[k[i]][2]),end = "")
			if noisy: print("Checking position 4, {} =?= {}".format(tiles[k[i]][3],tiles[k[j]][2]))
			if tiles[k[i]][3] == tiles[k[j]][2]:
				udans.append("{}{}".format(k[i],k[j]))				
				if noisy: print(" YES Uadding {}{} from val:{}".format(k[i],k[j],tiles[k[i]][3]),end = "")
			if noisy: print("")
	return (lrans, udans)



def solvea(lines, noisy=False):
	'''orient tiles so they all fit into square
	return 4 corners multiplied together
	tiles can be rotated, and align on all middle joints
	'''
	ans = 1
	t = {} # tile
	i = 0 # tile index
	loft = 0 # line of each tile
	r = [] # in this order, up to down
	l = [] # up to down
	u = [] # left to right
	d = [] # left to right
	for i in range(0,len(lines),12):
		r,l,u,d=[],[],[],[]
		# ~ if noisy: print("i={}, tileline={}".format(i,lines[i]))
		j1,tn = lines[i].split(" ")
		tn = tn[:-1] # tile number = tn
		# ~ if noisy: print("new tile #{}".format(tn))
		loft = 0
		u = list(lines[1+i])
		d = list(lines[10+i])
		# ~ print("u={} lines[{}]{}".format(u,i+9,lines[1+i]))
		# ~ print("d={} lines[{}]{}".format(d,i+9,lines[i+9]))
		for ii in range(10):
			r.append(lines[i+ii+1][-1])
			l.append(lines[i+ii+1][0])
		t["t{}p1".format(tn)] = (l,r,u,d)
		t["t{}p2".format(tn)] = (d,u,l[::-1],r[::-1])
		t["t{}p3".format(tn)] = (r[::-1],l[::-1],d[::-1],u[::-1])
		t["t{}p4".format(tn)] = (u[::-1],d[::-1],r,l)
		# ~ if noisy: print("t{}p1{}".format(tn,t["t{}p1".format(tn)]))
		# ~ if noisy: print("t{}p2{}".format(tn,t["t{}p2".format(tn)]))
		# ~ if noisy: print("t{}p3{}".format(tn,t["t{}p3".format(tn)]))
		# ~ if noisy: print("t{}p4{}".format(tn,t["t{}p4".format(tn)]))
	# ~ # now find all the l/r u/d matches from uniq keys
	if noisy: print("full set of t={}".format(t))
	lr,ud = findlrs(t, noisy)
	for l in lr:
		print("found lr {}".format(l))
	for u in ud:
		print("found ud {}".format(u))
	return ans

def returnnumcombos(list, noisy=False):
	''' drop a number if you can for all combos, return qty 
	4, 5, 6, 7 is mult 4:
	4, 5, 7
	4, 6, 7
	4, 5, 6, 7
	4, 7
	
	10, 11, 12 is mult 2:
	10, 11, 12
	10, 12
	'''
	combos = 1
	low =0
	high = len(list) -1
	
	if noisy: print("returnnumbercombos got {}".format(list))
	if len(list) < 3:
		if noisy: print("little fish, throw it back (1)\n")
		return 1
	while (low < high - 1):
		if low + 5 <= high and list[low] + 5 == list[high]:
			print("CR**, we hit a 6 high one")
		elif low + 4 <= high and list[low] + 4 == list[high]: #  5 in a row
			if noisy: print("FIVE low+4<=high, {}+3=={}".format(list[low],list[high]))
			combos *= 7
			low += 4
		elif low + 3 <= high and list[low] + 3 == list[high]: # 4 in a row
			if noisy: print("FOUR low+3<=high, {}+3=={}".format(list[low],list[high]))
			combos *= 4
			low += 2
		elif low + 2 <= high and list[high] - list[low] == 2 or list[high] - list[low] == 3:
			if noisy: print("THREE low+3<=high, {}+3=={}".format(list[low],list[high]))
			combos *= 2
			low += 1
		else:
			low += 1
		
	if noisy: print("sending back {} for this set\n".format(combos))
	return combos
	# take a low index and high one
	# if the high one is +2 or +3 in value, and there is exactly one
	#   value betweent the two, add 2 to this set 
	# if the value of the array element 2 above me is 2-3, then add 2 to multipler

	
def solveb(lines, noisy=False):
	if noisy: print("def solveb")
	''' find the number of combinations, still limited to 1, 2, or 3 diffs
	chains can go from 0 to max
	if a series goes from 2-3 in 3-4 positions, then it can be reduced
	 to a single set with a number of combinations in it, mutliply all these count(sets) together and you have an answer
	'''
	# break groups into sets that have >= 3 between edges
	edges = []
	slines = [0]
	low = 0
	ans = 1
	slines = slines + sorted(lines)
	mjolt = slines[-1] + 3
	slines = slines + [mjolt]
	if noisy: print("slines = {}".format(slines))
	for i in range(len(slines) - 1):
		#if noisy: print("i={}, with {} {}".format(i,slines[i+1], slines[i]))
		if slines[i + 1] - slines[i] >= 3 :
			if noisy: print("YEP {}".format(i))
			edges.append(i)
	for i in edges:
		# if noisy: print("edges processed {}".format(i))
		ans *= returnnumcombos(slines[low:i + 1], noisy)
		low = i
		
		
	return ans
	
if __name__ == "__main__":
	lines = getlinesfromfile("20ex1.txt")
	ansa = solvea(lines, noisy=True)
	print("20a: {}".format(ansa))
	print("solution:\n1951    2311    3079\n2729    1427    2473\n2971    1489    1171")
	# ~ ans = solveb(lines, noisy=False)
	# ~ print("10b: {}".format(ans))
	
# ~ 1951    2311    3079
# ~ 2729    1427    2473
# ~ 2971    1489    1171

# ~ found lr t1951p1t2311p1
# ~ found lr t2311p1t3079p3
# ~ found lr t1427p4t2311p4
# ~ found lr t2729p4t1951p4
# ~ found lr t2729p1t1427p1
# ~ found ud t1427p1t2311p1
# ~ found ud t1951p2t2311p2
# ~ found ud t2311p3t1427p3
# ~ found ud t2311p4t1951p4
# ~ found ud t2729p1t1951p1
# ~ found ud t1951p3t2729p3
# ~ found ud t2473p4t1171p1
# ~ found ud t1171p2t1489p4
# ~ found ud t1171p3t2473p2
# ~ found ud t2729p2t1427p2
# ~ found ud t1427p4t2729p4

