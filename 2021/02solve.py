#!/usr/bin/python -Wall

# f = open("02inp.txt", "r")
# # f = open("test.txt", "r", newline=None)
# fwd = 0
# depth = 0
# amt = 0
# for l in f:
#     l = l.rstrip()
#     d, b  = l.split(' ')
#     amt = int(b)
#     if d == 'down':
#         depth += amt
#     elif d == 'up':
#         depth -= amt
#         if depth < 0:
#             depth = 0
#     elif d == 'forward':
#         fwd += amt
#     else:
#         print("I'm lost")

# print('ans = {}'.format(fwd*depth))

# f.close() 


f = open("02inp.txt", "r")
# f = open("test.txt", "r", newline=None)
fwd = 0
depth = 0
aim = 0
amt = 0
for l in f:
    l = l.rstrip()
    d, b  = l.split(' ')
    amt = int(b)
    if d == 'down':
        aim += amt
    elif d == 'up':
        aim -= amt
    elif d == 'forward':
        fwd += amt
        depth += aim * amt
        # depth -= aim * amt
        if depth < 0:
            depth = 0
    else:
        print("I'm lost")

print('ans = {}'.format(fwd*depth))

f.close() 
