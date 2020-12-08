#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def passportscan(lines, validate = False, noisy = False):
    currentpassport = []
    a = 0
    for l in lines:
        if (l == ""): # blank line
            if validate:
                a += checkrequiredfieldsbetter(currentpassport, noisy)
            else:
                a += checkrequiredfields(currentpassport, noisy)
            currentpassport = []
        else:
            currentpassport.append(l)
    if validate:
        a += checkrequiredfieldsbetter(currentpassport, noisy)
    else:
        a += checkrequiredfields(currentpassport, noisy)
    return a

def checkrequiredfields(a, noisy = False):
    '''Quick check if all fields are in the record
    '''
    d = []
    for b in a:
        for c in b.split(" "):
            if noisy: print("k:v expected {}".format(c))
            k, v = c.split(":")
            d.append(k)
    for e in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if noisy: print("checking if {} is in the list {}".format(e, d))
        if e not in d:
            return 0
    return 1

def validatefield(k, v, noisy = False):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    if noisy: print("in validatefield with k={}, v={}".format(k, v))
    if (k == "byr"):
        if (v.isdigit and int(v) >= 1920 and int(v) <= 2002):
            return True
    elif k == "iyr":
        if (v.isdigit and int(v) >= 2010 and int(v) <= 2020):
            return True
    elif k == "eyr":
        if (v.isdigit and int(v) >= 2020 and int(v) <= 2030):
            return True
    elif k == "hgt":
        if "cm" in v:
            p1 = v.split("cm")[0]
            if p1.isdigit and int(p1) >= 150 and int(p1) <= 193:
                return True
        elif "in" in v:
            p1 = v.split("in")[0]
            if p1.isdigit and int(p1) >= 59 and int(p1) <= 76:
                return True
    elif k == "hcl":
        if (v[0] != "#"): return False
        if (len(v[1:]) != 6): return False
        for x in v[1:]:
            if not(x.isdigit()) and not(x in ('a', 'b', 'c', 'd', 'e', 'f')):
                return False
        return True
    elif k == "ecl":
        if v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return True
    elif k == "pid":
        if noisy: print("pid check len and digits, len={}".format(len(v)))
        if len(v) == 9:
            for x in v:
                if not(x.isdigit):
                    return False
            return True
    elif k == "cid":
        return True
    return False
    
    
def checkrequiredfieldsbetter(a, noisy=False):
    ''' fully validate each field except cid and only return 1 if all OK
    0 if not
    '''
    if noisy: print("in checkrequiredfieldsbetter a={}".format(a))
    d = []
    for b in a:
        for c in b.split(" "):
            if noisy: print("k:v expected {}".format(c))
            k,v = c.split(":")
            if (not(validatefield(k, v, noisy))):
                return 0
            d.append(k)
    for e in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if noisy: print("checking if {} is in the list {}".format(e,d))
        if e not in d:
            return 0
    return 1    

if __name__ == "__main__":
    pp = getlinesfromfile("4.txt")
    ans = passportscan(pp,validate=False,noisy=False)
    print("4a: {}".format(ans))
    ans = passportscan(pp, validate=True,noisy=False)
    print("4b: {}".format(ans))
    
    
