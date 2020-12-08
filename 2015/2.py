#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def smallestside(l, w, h):
	return sorted((l*w, w*h, h*l))[0]

def solvea(input):
	''' wrap presents each line = l x w x h in feet, without spaces
	take smallest one of (l*w | w*h | h*l) 
	and add it to 2(l*w + w*h + h*l) on each gift
	'''
	es = 0
	ans = 0
	for a in input:
		l,w,h = a.split("x")
		l = int(l)
		w = int(w)
		h = int(h)
		es = smallestside(l,w,h)
		ans += es + 2*(l*w + w*h + h*l)
	return ans;

def ribbenwrap(l,w,h):
	ord = sorted((int(l),int(w),int(h)))
	return 2 * (ord[0] + ord[1])

def ribbenbow(l,w,h):
	ord = sorted((int(l),int(w),int(h)))
	return l * w * h
	
def solveb(input):
	''' The ribbon required to wrap a present is the shortest distance 
	around its sides, or the smallest perimeter of any one face. Each 
	present also requires a bow made out of ribbon as well; the feet of
	 ribbon required for the perfect bow is equal to the cubic feet of 
	 volume of the present.
	 Ex: 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
	 plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
	'''
	es = 0
	ans = 0
	for a in input:
		l,w,h = a.split("x")
		l = int(l)
		w = int(w)
		h = int(h)
		ans += ribbenwrap(l, w, h) + ribbenbow(l, w, h)
	return ans;

if __name__ == "__main__":
    # lines.sort() # sorts in place, no return value
    lines = getlinesfromfile("2.txt")
    print("2a: Found: {}".format(solvea(lines)))
    print ("2b: Found: {}".format(solveb(lines)))
