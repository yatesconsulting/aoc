#!/usr/bin/python3

import itertools

def getlinesfromfile(filename):
    lines = []
    
    infile = open(filename, 'r')
    lines = [int(line) for line in infile.readlines()]
    infile.close()
    return lines

    
def solvea(lines, noisy=False):
    '''put all adapters in order 
     note which are only 1 diff in the sec and which are 3
    return the number of 1 differences * (3 diffs + 1)
    '''
    ones = 0 
    threes = 1 # one extra at end
    slines = sorted(lines)
    lastnum = 0 # this can only be 1-3, but we're not checking
    if noisy: print("l0 = {}".format(lastnum))
    for l in slines:
        if noisy: print("l = {}".format(l))
        if l - lastnum == 1:
            ones += 1
            if noisy: print("ones += 1 to {}".format(ones))
        elif l - lastnum == 3:
            threes += 1
            if noisy: print("threes += 1 to {}".format(threes))
        else:
            print("Probably an error")
        lastnum = l
    if noisy: print("returning ones {} * ( threes {})".format(ones, threes))
    return ones * threes

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
    lines = getlinesfromfile("10.txt")
    ansa = solvea(lines, noisy=False)
    print("10a: {}".format(ansa))
    ans = solveb(lines, noisy=False)
    print("10b: {}".format(ans))
