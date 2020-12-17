#!/usr/bin/python3

def getlinesfromfile(filename):
    lines = []
    infile = open(filename, 'r')
    lines = infile.read().splitlines()
    infile.close()
    return lines

def movesome(idir, cmddir, qty, noisy):
    x = 0
    y = 0
    if cmddir == 'F':
        cmddir = idir
    if cmddir == 'N':
        y = qty
    elif cmddir == 'S':
        y -= qty
    elif cmddir == 'E':
        x = qty
    elif cmddir == 'W':
        x -= qty
    else:
        print("real problem here {}{}".format(cmddir,qty))
    return [x, y]

def rotate(idir, cmd, deg, noisy):
    rtclick = {}
    ans = idir
    deg = int(deg)
    rtclick["E"] = "S"
    rtclick["S"] = "W"
    rtclick["W"] = "N"
    rtclick["N"] = "E"
    if cmd == "R":
        for i in range(int(deg/90)):
            ans = rtclick[ans]
    elif cmd == "L":
        for i in range(4 - int(deg/90)):
            ans = rtclick[ans]
    return ans

    
def solvea(lines, direction, noisy=False):
    '''
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

    '''
    if noisy: print("def solvea dir={}".format(direction))
    x = 0
    y = 0
        
    for l in lines:
        p1 = l[0]
        p2 = int(l[1:])
        if p1 == "R" or p1 == "L":
            direction = rotate(direction, p1, p2, noisy)
            if noisy: print("{} dir dir {}".format(l, direction))
        else:
            xd, yd = movesome(direction, p1, p2, noisy)
            x += xd
            y += yd
            if noisy: print("{} moved us {},{} to {},{}".format(l,xd,yd,x,y))
    return abs(x) + abs(y)

def movesome2(wx, wy, cmddir, qty, noisy):
    x = 0
    y = 0
    if cmddir == 'F':
        x = wx * qty
        y = wy * qty
    elif cmddir == 'N':
        x = wx
        y = wy + qty
    elif cmddir == 'S':
        x = wx
        y = wy - qty
    elif cmddir == 'E':
        x = wx + qty
        y = wy
    elif cmddir == 'W':
        x = wx - qty
        y = wy
    else:
        print("real problem here {}{}".format(cmddir, qty))
    return [x, y]


def resetvector(wx, wy, cmd, deg, noisy):
    if noisy: print("sub resetvector wx, wy, cmd, deg = {},{} {}{}".format(wx, wy, cmd, deg))
    if cmd == "R":
        for i in range(int(deg/90)):
            t = wx
            wx = wy
            wy = -t
    elif cmd == "L":
        for i in range(4 - int(deg/90)):
            t = wx
            wx = wy
            wy = -t
    return wx, wy
    
def solveb(lines, wx, wy, noisy=False):
    if noisy: print("def solveb")
    ''' 
    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. 
The waypoint is relative to the ship; that is, if the ship moves, the 
waypoint moves with it.
    '''
    if noisy: print("def solveb vector={},{}".format(wx, wy))
    x = 0
    y = 0
    d = []
    for l in lines:
        p1 = l[0]
        p2 = int(l[1:])
        if p1 == "R" or p1 == "L":
            wx, wy = resetvector(wx, wy, p1, p2, noisy)
            if noisy: print("{} new wx,wy {},{}".format(l, wx, wy))
        elif p1 in ("N", "S", "E", "W"):
            wx, wy = movesome2(wx, wy, p1, p2, noisy)
            if noisy: print("{} vector changed {},{}".format(l,wx,wy))            
        elif p1 == "F":
            xd, yd = movesome2(wx, wy, p1, p2, noisy)
            x += xd
            y += yd
            if noisy: print("{} moved us {},{} to {},{}".format(l,xd,yd,x,y))
        else:
            print("big2 trouble here")
    return abs(x) + abs(y)
        
if __name__ == "__main__":
    lines = getlinesfromfile("12.txt")
    # ~ print (lines)
    ansa = solvea(lines, "E", noisy=False)
    print("12a: {}".format(ansa))
    ans = solveb(lines, 10, 1, noisy=False)
    print("12b: {}".format(ans))
