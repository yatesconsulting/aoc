#!/usr/bin/python -Wall

# f = open("06inp.txt", "r")
# # f = open("test.txt", "r", newline=None)
# all=[]

# line=a=b=b1=0
# cards = []
# cardsindex = 0
# onecard = []
# ans = {}
# m = b = None
# for l in f:
#     l = l.strip()
#     allfish = [int(r) for r in l.split(",")]
#     # print(allfish)

# ngen = []
# for i in range(80):
#     ngen = []
#     for fish in allfish:
#         if fish == 0:
#             ngen.append(6)
#             ngen.append(8)
#         else:
#             ngen.append(fish-1)
#     allfish = ngen[:]
# print(len(allfish))

        

   

# f.close() 


f = open("06inp.txt", "r")
# f = open("test.txt", "r", newline=None)

ans = [0,0,0,0,0,0,0,0,0]
for l in f:
    l = l.strip()
    for n in [int(r) for r in l.split(",")]:
        ans[n] += 1

# ngen = [0,0,0,0,0,0,0,0,0]
print("ans = {}".format(ans))
for i in range(256):
    ngen = [0,0,0,0,0,0,0,0,0]
    ngen[0] = ans[1]
    ngen[1] = ans[2]
    ngen[2] = ans[3]
    ngen[3] = ans[4]
    ngen[4] = ans[5]
    ngen[5] = ans[6]
    ngen[6] = ans[7] + ans[0]
    ngen[7] = ans[8]
    ngen[8] = ans[0]
    ans = ngen.copy()
print(sum(ans)) # 26984457539 too low


f.close() 
