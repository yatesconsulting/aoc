#!/usr/bin/python -Wall

def showit(it):
    ans = ""
    xmx = [int(i.split(',')[0]) for i in it.keys()]
    ymx = [int(i.split(',')[1]) for i in it.keys()]
    for y in range(max(ymx)+1):
        for x in range(max(xmx)+1):
            key = '{},{}'.format(x,y)
            if key in it:
                ans += "{}".format(it[key]) 
            else:
                ans += "."
        ans += "\n"
    return ans
    
f = open("05inp.txt", "r")
# f = open("tes?t.txt", "r", newline=None)
all=[]

line=a=b=b1=0
cards = []
cardsindex = 0
onecard = []
ans = {}
m = b = None
for l in f:
    l = l.strip()
    x1y1,x2y2 = l.split(" -> ")
    x1,y1 = x1y1.split(',')
    x2,y2 = x2y2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    k = ""
    yl = yh = xl = xh = None
    # print('{} = {} {} {} {}'.format(l,x1,y1,x2, y2))
    if x1 == x2:
        if y1 < y2:
            yl = y1
            yh = y2 + 1
        else:
            yl = y2
            yh = y1  + 1
        for y in range(yl,yh):
            # print('{} . x{} y{}'.format(l,x1,y))
            k =  '{},{}'.format(x1,y)
            if k in ans:
                ans[k] += 1
            else:
                ans[k] = 1
    elif y1 == y2:
        if x1 < x2:
            xl = x1
            xh = x2 + 1
        else:
            xl = x2
            xh = x1  + 1
        for x in range(xl,xh):
            # print('{} . x{} y{}'.format(l,x,y1))
            k =  '{},{}'.format(x,y1)
            if k in ans:
                ans[k] += 1
            else:
                ans[k] = 1
    elif abs(y1-y2) == abs(x1-x2):
        # print("adding info for {}".format(l))
        # y = mx + b
        m = int((y2-y1)/(x2-x1))
        b = y1 - m * x1
        # print("y = mx+b = {}x + {}".format(m, b))
        if x1 < x2:
            xr = range(x1,x2+1)
        else:
            xr = range(x1,x2-1,-1)
        # print('xr: {}'.format(xr))
        
        for x in xr:
            y = m * x + b
            # print('x{} y{}'.format(x,y))
            k =  '{},{}'.format(int(x),int(y))
            if k in ans:
                ans[k] += 1
            else:
                ans[k] = 1


# print('ans = {}'.format(ans))
cntans = [l for l in ans.values() if l >= 2]
# print(showit(ans))
print("count = {}".format(len(cntans))) # 53406 too high part 2, 21488 too low

f.close() 
