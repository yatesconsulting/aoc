#!/usr/bin/python -Wall

from numpy import mean

f = open("07inp.txt", "r")
# f = open("test.txt", "r", newline=None)

for l in f:
    l = l.strip()
    puz = [int(r) for r in l.split(",")]
#     # print(allfish)

qty ={}
for p in puz:
    if p in qty:
        qty[p] += 1
    else:
        qty[p] = 1 

def distto(target,fromdict):
    ans = 0
    for k,v in fromdict.items():
        m = abs(k-target) * v
        ans += m
    return ans

def dailysum(n):
    return n/2*(n+1)
        
def distto2(target,fromdict):
    ans = 0
    step = 1
    for k,v in fromdict.items():
        m = dailysum(abs(k-target)) * v 
        ans += m
    return ans

ans = 0
valofmax = []
minv = min(qty)
maxv = max(qty)

anslongway = {}
for i in range(minv,maxv + 1):
    # anslongway[i] = distto(i,qty)
    anslongway[i] = distto2(i,qty)
    

distans = min(anslongway.values())
keyans = [i for i in anslongway if anslongway[i] == distans]

print("distans = {} keyans {} ".format(distans, keyans)) # distans 325528 correct


f.close() 

