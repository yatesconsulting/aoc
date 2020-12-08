#!/usr/bin/python3
import re

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def findlinesthatmeetcriteria(lines):
    ''' lines = A-B C: DDDD
    where A and B are numbers with B > A
    C is a single letter
    DDDD is a password
    the criteria is met if the number of C's in DDDD is A - B inclusive
    '''
    ans = 0
    for x in lines:
        
       a,b,c,d = x.replace("-"," ").replace(":","").split(' ')
       # print("splitting {} into {},{},{}, and {}".format(x,a,b,c,d))
       if (c in d):
           cnt = len(re.findall(c,d))
           if (cnt >= int(a) and cnt <= int(b)):
               ans += 1
    return ans

def findlinesthatmeetcriteriab(lines):
    ''' lines = A-B C: DDDD
    where A and B are numbers with B > A
    C is a single letter
    DDDD is a password
    the criteria is met if the Ath character of DDDD = C or
    the Bth character of DDDD = C, but not both (or neither)
    
    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    '''
    ans = 0
    for x in lines:
        
       a,b,c,d = x.replace("-"," ").replace(":","").split(' ')
       # print("splitting {} into {},{},{}, and {}".format(x,a,b,c,d))
       if (c in d):
           c1 = d[int(a)-1] # 1 indexed
           c2 = d[int(b)-1]
           # ^ = boolean logic xor, exactly one true
           if ((c1 == c) ^ (c2 == c)): 
               ans += 1
    return ans

if __name__ == "__main__":
    lines = getlinesfromfile("2.txt")
    print("2a: {}".format(findlinesthatmeetcriteria(lines)))
    print("2b: {}".format(findlinesthatmeetcriteriab(lines)))
