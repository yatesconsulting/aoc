#!/usr/bin/python -Wall

# # f = open("01inp.txt", "r")
# f = open("inp.txt", "r")
# firstline = True
# lv = 0
# largercount = 0
# for x in f:
#     v = int(x)
#     if not firstline:
#         if v > lv:
#             largercount += 1
#     else:
#         firstline = False
#     lv = v
    

# print(largercount)
# f.close() 


f = open("01inp.txt", "r")
# f = open("inp.txt", "r")
linenum = 0
first3lines = True
lv = 0
lv2 = 0
lv3 = 0

largercount = 0
for x in f:
    v = int(x)
    a = v + lv + lv2
    b = lv + lv2 + lv3
    # print ("line {} has vals v... {},{},{},{} for A{} B{}".format(linenum, v, lv, lv2, lv3, a, b))
    linenum += 1
    if linenum > 3:
        if a > b:
            print("yup")
            # line{} has {} > {}".format(linenum, a, b))
            largercount += 1
    lv3 = lv2
    lv2 = lv
    lv = v
    
print(largercount)
f.close() 
