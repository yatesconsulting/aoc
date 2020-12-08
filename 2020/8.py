#!/usr/bin/python3

def getlinesfromfile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def solvea(lines, noisy=False):
    '''acc increases or decreases a single global value called the 
    accumulator by the value given in the argument. For example, acc +7 
    would increase the accumulator by 7. The accumulator starts at 0. 
    After an acc instruction, the instruction immediately below it is 
    executed next.
    
    jmp jumps to a new instruction relative to itself. The next 
    instruction to execute is found using the argument as an offset from
    the jmp instruction; for example, jmp +2 would skip the next 
    instruction, jmp +1 would continue to the instruction immediately 
    below it, and jmp -20 would cause the instruction 20 lines above to 
    be executed next.
    
    nop stands for No OPeration - it does nothing. The instruction 
    immediately below it is executed next
    w
    ex1 = 5, the value of accumulator just before entering an infinate 
    loop (the same line twice) 
    '''
    accumulator = 0
    lineflag = {}
    linenumber = 0
    if noisy: print("def solvea")
    while (linenumber < len(lines)):
        (verb,num) = lines[linenumber].split(" ")
        num = int(num)
        if noisy: print("ln={} verb={}, num={}, lineflag={}".format(linenumber, verb, num, lineflag))
        if verb== "acc":
            accumulator += num
            if noisy: print("verb=acc, accumulator now={}".format(accumulator))
            linenumber += 1
        elif verb == "nop":
            if noisy: print("verb=nop")
            linenumber += 1
        elif verb == "jmp":
            if noisy: print("verb=jmp")
            linenumber += num
        if linenumber in lineflag.keys():
            return accumulator
        else:
            lineflag[linenumber] = 1
    print("8b: solution found: {}".format(accumulator))
    return False

def solveb(lines, noisy=False):
    if noisy: print("def solveb")
    ''' if you change one nop to jmp or jmp to nop, it will run through the list
    and exit, ans = val of accumulator at that time
    '''
    c = lines.copy()
    for i in range(len(lines)):
        (verb,num) = lines[i].split(" ")
        if noisy: print("ln={} verb={}".format(linenumber, verb))
        if verb== "jmp":
            c[i] = lines[i].replace('jmp','nop')
            if solvea(c, noisy=noisy):
                c[i] = lines[i]
            else:
                return
        elif verb == "nop":
            c[i] = lines[i].replace('nop','jmp')
            if solvea(c, noisy=noisy):
                c[i] = lines[i]
            else:
                return
    return "sorry, we failed"

if __name__ == "__main__":
    lines = getlinesfromfile("8.txt")
    ans = solvea(lines, noisy=False)
    print("8a: {}".format(ans))
    ans = solveb(lines, noisy=False)
    print("8b: read the answer above")
