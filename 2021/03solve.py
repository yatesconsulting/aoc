#!/usr/bin/python -Wall

# f = open("03inp.txt", "r")
# # f = open("test.txt", "r", newline=None)
# d=e=[0,0,0,0,0,0,0,0,0,0,0,0]

# lines=a=b=0
# for l in f:
#     l = l.strip()
#     d = list(l)
#     for i in range(len(d)):
#         e[i] += int(d[i])
#     lines += 1

# f.close() 

# for i in range(len(d)):
#     amt = 2**(len(d)-i-1)
#     if e[i]*2 > lines:
#         a += amt
#     else:
#         b += amt
# print("e0={}".format(e[0]))
# print ("{}*{}={} from lines {}".format(a,b,a*b, lines)) # 4192256 wrong guess 1

def bitqty(numlist, bit):
    lenl = len(numlist)
    bitlist = [int(x[bit]) for x in numlist]
    if sum([int(d) for d in bitlist]) * 2 > lenl:
        return 1
    elif sum(bitlist) * 2 == lenl:
        return 2
    else:
        return 0

def bitmatchonly(numlist, bit, zeroorone):
    # print("\nlooking at list {} for bit number {} to match {}".format(numlist, bit, zeroorone))
    ans = [ x for x in numlist if int(x[bit]) == zeroorone ]
    # print("\nand I found {}".format(ans))
    return ans

f = open("03inp.txt", "r")
# f = open("test.txt", "r", newline=None)
all=[]

lines=a=b=b1=0
for l in f:
    l = l.strip()
    d = list(l)
    b1 += int(d[0])
    all.append(d)
    lines += 1

# 1st time, just use b1, maybe
o2 = all[:]
co2 = all[:]
votestoabort = 0

for bit in range(len(all[0])):
    if votestoabort == 2:
        break
    if len(o2) > 1:
        o2bit = bitqty(o2, bit)
        # print ("o2bit: {}".format(o2bit))
        if o2bit == 2:
            o2bit = 1
        o2 = bitmatchonly(o2, bit, o2bit)
        if len(o2) == 1:
            votestoabort += 1
    if len(co2) > 1:
        bs = bitqty(co2, bit)
        if bs == 2 or bs == 1:
            co2bit = 0
        else:
            co2bit = 1 
        co2 = bitmatchonly(co2, bit, co2bit)
        if len(co2) == 1:
            votestoabort += 1
    # print ("bit: {} lens: co2 {} o2 {}".format(bit, len(co2),len(o2)))

co2d = int(''.join(co2[0]),2)
o2d = int(''.join(o2[0]),2)
print ("ans = {} * {} = {}".format(co2d, o2d, co2d * o2d))

f.close() 
