#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def counttreeshit(hill,right,down,output=0):
    ''' How many trees will you hit?
    Use hill from filename, but repeats to the right
    Start in the upper left and each move is in a step of right, down
    count trees until you hit bottom of file
    '''
    x = 0
    y = 0
    a = 0
    widthmod = len(hill[y]) 
    rows = len(hill)
    while y < rows:
        # look at current location on map, is it a tree?
        #print ("{},{}\n{}".format(x,y,hill[y]))
        if ((hill[y])[x] == "#"):
            if output:
                print ("{} {},{}".format((hill[y][:x]+"X"+hill[y][x+1:]), x, y))
            a += 1
        else:
            if output:
                print ("{} {},{}".format((hill[y][:x]+"O"+hill[y][x+1:]), x, y))
            
        # move the coordinates
        y += down
        x = (x + right) % widthmod
        #print ("new location: {},{}".format(x,y))
    return a

if __name__ == "__main__":
    hill = getlinesfromfile("3.txt")
    ans = counttreeshit(hill,3,1)
    print("3a: {}".format(ans))
    ans *= counttreeshit(hill,1,1)
    ans *= counttreeshit(hill,5,1)
    ans *= counttreeshit(hill,7,1)
    ans *= counttreeshit(hill,1,2)
    print("3b: {}".format(ans))
