print("hi")

with open('1a.csv') as f:
    lines = f.read().splitlines()

# lines.sort()

# for x in sorted(lines, reverse=True):
for x in lines:
    y = 2020 - int(x)
    # print("x={}, y={}".format(x,y))
    if str(y) in lines:
        print ("Found {} * {} = {}".format(x,y,int(x)*y))



