#!/usr/bin/python3

def getlinesfromfile(filename):
    with open('1a.csv') as f:
        lines = f.read().splitlines()
    return lines

def findproductoftwothatsum2020(lines):
    for x in lines:
        y = 2020 - x
        if y in lines:
            return x * y

def intallvals(lines):
    l3 = [int(numeric_string) for numeric_string in lines]
    return l3

def sumsof2numberslessthan2020(lines):
    a = []
    b = []
    fa = []
    for x in sorted(lines):
        for y in sorted(lines, reverse=True):
            if x + y < 2020:
                a.append(x+y)
                b.append("{},{}".format(x,y))
    for i in range(len(a)):
        if (a[i] < 2020 and 2020 - a[i]) in lines:
            a1 = 2020-a[i]
            a2,a3 = b[i].split(",")
            return a1 * int(a2) * int(a3)


if __name__ == "__main__":
    # lines.sort() # sorts in place, no return value
    lines = getlinesfromfile("1a.csv")
    lines = intallvals(lines)
    print("1a: Found: {}".format(findproductoftwothatsum2020(lines)))
    print ("1b: Found: {}".format(sumsof2numberslessthan2020(lines)))
