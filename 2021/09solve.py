#!/usr/bin/python -Wall

# f = open("09inp.txt", "r")
f = open("test.txt", "r", newline=None)

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist, you passed {} in {}".format(val, my_dict)

m = []
ans = 0
ansb = 0
basin = []
pos = []

for l in f:
    l = l.strip()
    a = [int(l) for l in list(l)]
    m.append(a)
    # print("l={}".format(a))
    # 123
    # 111

# line = 0
leny = len(m)
lenx = len(m[0])
# remember that m is m[y][x], (backwards)
for y in range(leny):
    # print ("Y{}: {}".format(line, m[y]))
    # line += 1
    for x in range(lenx):
        ck = []
        # print("elem {}".format(m[y][x]))
        if x == 0 and y == 0: # upper left corner
            ck.append(m[1][0])
            ck.append(m[0][1])
            # print ("upper left corner {}".format(ck))
        elif x == 0 and y == leny-1: # lower left corner
            ck.append(m[y][1])
            ck.append(m[y-1][0])
            # print ("lower left corner{}".format(ck))
        elif x == lenx-1 and y == 0: # upper right corner
            ck.append(m[0][x-1])
            ck.append(m[1][x])
            # print ("upper right corner{}".format(ck))
        elif x == lenx-1 and y == leny-1: # lower right corner
            ck.append(m[y][x-1])
            ck.append(m[y-1][x])
            # print ("lower right corner{}".format(ck))
        elif x == lenx-1: # right edge
            ck.append(m[y-1][x])
            ck.append(m[y][x-1])
            ck.append(m[y+1][x])
            # print ("right edge{}".format(ck))
        elif x == 0: # left edge
            ck.append(m[y-1][0])
            ck.append(m[y][1])
            ck.append(m[y+1][0])
            # print ("left edge{}".format(ck))
        elif y == leny -1: # bottom
            ck.append(m[y][x-1])
            ck.append(m[y-1][x])
            ck.append(m[y][x+1])
            # print ("bottom edge{}".format(ck))
        elif y == 0: # top edge
            ck.append(m[0][x-1])
            ck.append(m[1][x])
            ck.append(m[0][x+1])
            # print ("top edge{}".format(ck))
        else:
            ck.append(m[y][x-1])
            ck.append(m[y-1][x])
            ck.append(m[y+1][x])
            ck.append(m[y][x+1])
            # print ("all they way around{}".format(ck))

        # print ("[{},{}] {} with neighbors {}".format(y, x, m[y][x], ck))
        lessthans = []
        lessthans = [t for t in ck if t <= m[y][x]]
        # print("lessthans = {}".format(lessthans))
        # break
        if not lessthans:
            # print("Yup {} lessthans: {}".format(m[y][x], lessthans))
            ans += m[y][x] + 1
            pos.append("{},{}".format(x,y))
            # figure up how many are in this basin
            # for yy in range(y):
            #     for xx in range(x):
            #         pass # check from this point outward in 4 directions until each hits a 9, and each width along the way until you hit 9's

def xlrsweep (x, y, m):
    cnt = 1
    # sweep left from here
    xl = x -1
    while (xl >= 0 and m[y][xl] != 9):
        # print("{}".format(m[y][xl]))
        cnt += 1
        xl -= 1
    xr = x + 1
    while (xr < lenx and m[y][xr] != 9):
        # print("{}".format(m[y][xr]))
        cnt += 1 
        xr += 1
    print('swept x,y={},{} from {},{} with ans {}'.format(x,y, xl, xr, cnt))
    # a = input()
    return cnt

for pt in [pos[0]]:
    x,y = pt.split(',')
    x = int(x)
    y = int(y)
    print("114 {},{}".format(x,y))
    cnt1 = 0
    # sweep to the left and right of each up/down until 9s are encountered
    yt = y
    while (yt >= 0 and m[yt][x] != 9):
        print("118yt={}".format(yt))
        cnt1 += xlrsweep(x, yt, m)
        yt -= 1
    yt = y + 1
    print("yt={}, leny {}, m[yt][x] {}".format(yt, leny, m[yt][x]))
    while (yt < leny and m[yt][x] != 9):
        print("123yt={}".format(yt))
        cnt1 += xlrsweep(x, yt, m)
        yt += 1
    basin.append(cnt1)

print (basin)
    
            
print("part a: {}".format(ans))


f.close() 

