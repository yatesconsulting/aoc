#!/usr/bin/python -Wall

f = open("08inp.txt", "r")
# f = open("test.txt", "r", newline=None)

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist, you passed {} in {}".format(val, my_dict)

ans = 0
for l in f:
    l = l.strip()
    # bcedagf ebadf gcdfe gfcead bcedgf dfeca ac dgca ace cafbge | ecfdbag gecfd feadb degacbf

    lft,rt = l.split(' | ')
    nums = [''.join(sorted(l)) for l in lft.split(' ')]
    rtnums = [''.join(sorted(l)) for l in rt.split(' ')]
    lineans = {}
    segans = {}
    fives = []
    sixes = []
    for a in nums:
        if len(a) == 2:
            lineans[1] = a
        elif len(a) == 3:
            lineans[7] = a
        elif len(a) == 4:
            lineans[4] = a
        elif len(a) == 5:
            fives.append(a)
        elif len(a) == 6:
            sixes.append(a)
        elif len(a) == 7:
            lineans[8] = a
        else:
            print("HEY-what's up here? {}".format(len(a)))
    for s in fives:
        in1 = in4 = 0
        for c in s:
            if c in lineans[1]:
                in1 += 1
            if c in lineans[4]:
                in4 += 1
        if in1 == 2:
            lineans[3] = s
        elif in4 == 2:
            lineans[2] = s
        else:
            lineans[5] = s
    for s in sixes:
        in4 = in7 = 0
        # print("sixes: {}".format(s))
        for c in s:
            if c in lineans[4]:
                in4 += 1
            if c in lineans[7]:
                in7 += 1
        if in4 == 4:
            lineans[9] = s
        elif in7 == 2:
            lineans[6] = s
        else:
            lineans[0] = s
        
    tentothe = 3
    for r in rtnums:
        ans += 10 ** tentothe * get_key(r, lineans)
        tentothe -= 1
        # print (ans)
    # print(lineans)
    # print(rtnums)
print (ans) # 61229 too low
    # break

f.close() 

