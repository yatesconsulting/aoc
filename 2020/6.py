#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def tallyuniqs(group, noisy=False):
    if noisy: print("def tallyuniqs")
    tg = []
    b = []
    for a in group:
        b = []
        for b in a:
            if not(b == " "):
                tg.append(b)
    c = set(tg)
    return len(c)
        
def uniqletterspergroup(lines, noisy = False):
    if noisy: print("def uniqletterspergroup")
    group = []
    a = 0
    for l in lines:
        if (l == ""):
            a += tallyuniqs(group, noisy)
            group = []
        else:
            group.append(l)
    a += tallyuniqs(group, noisy)
    return a

def tallydups(group, noisy=False):
    if noisy: print("def tallydups, group={}".format(group))
    tg = []
    lg = []
    for i in range(len(group)):
        tg = list(group[i])
        if i > 0:
            a = set(tg)
            b = set(lg)
            if noisy: print("a={},b={}".format(a,b))            
            tg = list(set(tg) & set(lg))
        lg = tg
    if noisy: print("lentg={}".format(len(tg)))
    return len(tg)
    
def dupletterspergroup(lines, noisy=False):
    if noisy: print("def dupletterspergroup")
    group = []
    a = 0
    for l in lines:
        if (l == ""):
            a += tallydups(group, noisy)
            group = []
        else:
            group.append(l)
    a += tallydups(group, noisy)
    return a

if __name__ == "__main__":
    lines = getlinesfromfile("6.txt")
    ans = uniqletterspergroup(lines , noisy=False)
    print("6a: {}".format(ans))
    ans = dupletterspergroup(lines, noisy=False)
    print("6b: {}".format(ans))
