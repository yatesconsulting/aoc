#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def numpart(letters,lowerhalfchar,upperhalfchar, noisy=False):
    low = 0
    llen = len(letters)
    high = 2 ** llen - 1
    for i in range(llen - 1):
        a = letters[i]
        if a == lowerhalfchar: high = (high - low + 1)/2 + low - 1
        elif a == upperhalfchar: low = (high - low + 1)/2 + low
    return low if letters[llen - 1] == lowerhalfchar else high

def seatnumber(c, noisy=False):
    row = numpart(c[:7],"F","B")
    if noisy: print("row= {}".format(row))
    col = numpart(c[7:],"L","R")
    if noisy: print("col= {}".format(col))
    return row * 8 + col

def seatnumberorig(c, noisy=False):
    if noisy: print("def seatnumber c={}".format(c))
    low = 0
    high = 127
    for i in range(6):
        a = c[i]
        if a == "F": # lower half
            high = (high-low+1)/2+low-1
        elif a == "B": # upper half
            low = (high-low+1)/2 + low
    if c[6] == "F": # lower half
        row = low
    else:
        row = high
    if noisy: print("row= {}".format(row))

    low = 0
    high = 7
    for i in range(2):
        a = c[i+7]
        if a == "L": # lower half
            high = (high-low+1)/2+low-1
        elif a == "R": # upper half
            low = (high-low+1)/2 + low
    if c[9] == "L": #  lower half
        col = low
    else:
        col = high
    if noisy: print("col= {}".format(col))
    return row * 8 + col

def findhighestseat(lines, noisy=False):
    highest = 0
    sn = 0
    for l in lines:
        sn = seatnumber(l, noisy)
        if noisy: print("{} = {}".format(l,sn))
        if sn > highest:
            highest = sn
    return highest

def findmyseat(lines, noisy=False):
    seats = []
    for l in lines:
        sn = seatnumber(l, noisy)
        seats.append(sn)
    seats.sort()
    for a in range(len(seats)):
        if a > 0 and (seats[a] > (seats[a-1] + 1)):
            return seats[a]-1

if __name__ == "__main__":
    pp = getlinesfromfile("5.txt")
    ans = findhighestseat(pp,noisy=False)
    print("5a: {}".format(ans))
    ans = findmyseat(pp,noisy=False)
    print("5b: {}".format(ans))
    
