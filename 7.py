#!/usr/bin/python3

import re

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def getlinesfromfilepaulsway(filename):
    data = open(filename) \
        .read() \
        .split('\n\n')
    return data

def whatallbagscanholdthisbag(lines, bag, noisy=False):
    if noisy: print("def whatallbagscanholdthisbag")
    baglist = []
    bag = bag.replace("bags", "bag")
    for l in lines:
        if noisy: print("l of bag={}".format(l))
        left, right = l.split(" bags contain ")
        if noisy: print("left={},right={}".format(left,right))
        if bag in right:
            if noisy: print("appending {} holding shiny gold".format(left))
            baglist.append(left)
            baglist = baglist + (whatallbagscanholdthisbag(lines, left, noisy))
    return baglist
    
def solveparta(lines, bag, noisy=False):
    if noisy: print("def solveparta")
    a = whatallbagscanholdthisbag(lines, bag, noisy)
    if noisy: print ("FOUND: {}".format(a))
    b = set(a)
    return len(b)

def whatbagsmustthisbaghold(dictbags, bag, noisy=False):
    # if noisy: print("def whatbagsmustthisbaghold {}".format(bag))
    p = re.compile(' *bags*.*')
    ans = 1 # the passed bag counts as a bag
    for a in (dictbags[bag]):
        b, c = a.split(" ", 1)
        if b.isnumeric():
            qty = int(b)
            contents = p.sub('', c)
            if noisy: print("bag {} is qty=1 bag that contains qty={}, contents={}".format(bag, qty, contents))
            ans += (qty * whatbagsmustthisbaghold(dictbags, contents, noisy))
        else:
            # no other bags, not 1
            if noisy: print("bag {} is qty=1 bag {} has no numeric b".format(bag, a))
            ans += 0
    return ans
    
def solvepartb(lines, bag, noisy=False):
    if noisy: print("def solvepartb")
    # find the nubmer of bags required for the passed bag
    # add the number of bags in it and their bags, etc
    baglist = {}
    
    for l in lines:
        left, right = l.split(" bags contain ")
        rbags = right.split(", ")
        # if noisy: print("left={},rbags={}".format(left,rbags))
        baglist[left] = rbags
        # if noisy: print("baglist={}".format(baglist))
    if noisy: print("The bag list in better form is: {}".format(baglist))
    # ans - 1 because you don't count the outer bag
    ans = whatbagsmustthisbaghold(baglist, bag, noisy) - 1
    return ans

if __name__ == "__main__":
    lines = getlinesfromfile("7.txt")
    ans = solveparta(lines,"shiny gold", noisy=False)
    print("7a: {}".format(ans))
    # ~ ans = solvepartb(lines, "vibrant plum", noisy=True)
    # ~ print("7b: {}".format(ans))
    ans = solvepartb(lines, "shiny gold", noisy=False)
    print("7b: {}".format(ans))
