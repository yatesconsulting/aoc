#!/usr/bin/python3

def getlinesfromfile(filename):
    lines = []
    
    infile = open(filename, 'r')
    lines = [int(line) for line in infile.readlines()]
    infile.close()
    return lines

def checkthispreamble(preamble, num, noisy=False):
    '''solvea helper to see if this preamble works
    '''
    if noisy: print("def checkthispreamble preamble={}, num={}".format(preamble, num))
    for i in preamble:
        if num - i in preamble and num - i != i:
            return True
    return False
    
def solvea(lines, preamble, noisy=False):
    '''after the preamble, the number must be a sum of 2 other uniq 
    numbers in the current position preamble.
    answer is first one that is not valid, 127 in ex1
    '''
    i = preamble
    if noisy: print("def solvea preamble={}".format(preamble))
    while (i < len(lines)):
        if not checkthispreamble(lines[i - preamble:i], lines[i], noisy):
            return lines[i]
        i += 1
    return False

def solveb(lines, sum2me, noisy=False):
    if noisy: print("def solveb")
    ''' find the number list within lines that sum to sum2me, 
    ans = first and last in series 
    '''
    low = 0
    high = 1
    while (high < len(lines)):
        if noisy: print("low={}, high={}, lv={}, hv={}, ts={}, set={}".format(low,high,lines[low],lines[high],lines[low:high],sum(lines[low:high])))
        while (sum(lines[low:high]) < sum2me and low < high):
            high += 1
            if noisy: print("high+=1 low={}, high={}, lv={}, hv={}, ts={}, set={}".format(low,high,lines[low],lines[high],lines[low:high],sum(lines[low:high])))

        while (sum(lines[low:high]) > sum2me and low < high):
            low += 1
            if noisy: print("low+=1 low={}, high={}, lv={}, hv={}, ts={}, set={}".format(low,high,lines[low],lines[high],lines[low:high],sum(lines[low:high])))
        if low == high:
            high += 1
            if noisy: print("low==high+=1 low={}, high={}, lv={}, hv={}, ts={}, set={}".format(low,high,lines[low],lines[high],lines[low:high],sum(lines[low:high])))

        if  sum(lines[low:high]) == sum2me:
            if noisy: print("WIN! low={}, high={}, lv={}, hv={}, ts={}, set={}".format(low,high,lines[low],lines[high],lines[low:high],sum(lines[low:high])))
            a = sorted(lines[low:high])
            return a[0] + a[-1]
        high += 1
    return "sorry, we failed"

if __name__ == "__main__":
    lines = getlinesfromfile("9.txt")
    #ansa = 105950735
    #ansa = 127
    ansa = solvea(lines, 25, noisy=False)
    print("9a: {}".format(ansa))
    ans = solveb(lines, ansa, noisy=False)
    print("9b: {}".format(ans))
