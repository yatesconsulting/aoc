#!/usr/bin/python
import sys
import itertools 

class amplifier:
    def __init__(self, mydata, input, name):
        self.mydata = mydata
        self.lenmydata = len(mydata)
        self.rebootdata = mydata
        self.input = input
        self.position = 0
        self.output = []
        self.runningstatus = 1
        self.waitingoninput = 0
        self.name = name
        self.debug = 0
        
    def reboot(self):
        self.mydata = self.rebootdata
        self.position = 0
    
    def receiveinput(self,d):
        self.input.insert(0,d)

    def go(self):
        if (self.position < self.lenmydata):
            if self.debug: print(self.mydata)
            oc = self.mydata[self.position] % 10
            if self.mydata[self.position] > 100 and int(self.mydata[self.position]/100)%10 == 1:
                p1 = 1 # immediate
            else:
                p1 = 0 # positional
            if self.mydata[self.position] > 1000:
                p2 = 1
            else:
                p2 = 0
            if (4 == oc):
                if p1:
                    dout = self.mydata[self.position+1]
                else:
                    dout = self.mydata[self.mydata[self.position+1]]
                if self.debug: print ("{} OPCODE 4, output {}".format(self.name,dout))
                self.output.insert(0,dout)
                self.position += 2
            elif (3 == oc):
                # get input from somewhere, from other amplifier
                if self.debug: print ("{} OPCODE 3, pos27={} input len={} v={}".format(self.name,self.mydata[self.position+1],len(self.input),self.input))
                if (len(self.input) > 0):
                    inp = self.input.pop()
                    self.mydata[self.mydata[self.position + 1]] = inp
                    self.position += 2
                    self.waitingoninput = 0
                else:
                    self.waitingoninput = 1
                if self.debug: print("/OPCODE 3, waitingoninput={}".format(self.waitingoninput))
            elif (99 == self.mydata[self.position]):
                self.runningstatus = 0
            else:
                a = self.mydata[self.position+1]
                b = self.mydata[self.position+2]
                p = self.mydata[self.position+3] # always positional
                if self.debug: print ("{} setof4 ocfull:{},a:{},b:{},p:{},|,p1:{},p2:{}, position:{} all:\n{}".format(self.name,self.mydata[self.position],a,b,p,p1,p2,self.position,self.mydata))
                # 000oo
                if p1:
                    av = int(a)
                else:
                    av = int(self.mydata[a])
                if p2:
                    bv = int(b)
                else:
                    bv = int(self.mydata[b])
                #print ("av,bv={},{}".format(av,bv))
                if (1 == oc):
                    if self.debug: print ("{} OPCODE 1, putting {} + {} in position {}".format(self.name,av,bv,p))
                    self.mydata[p] = int(av) + int(bv)
                    self.position += 4
                elif (2 == oc):
                    if self.debug: print ("{} OPCODE 2, putting {} * {} in position {}".format(self.name,av,bv,p))
                    self.mydata[p] = int(av) * int(bv)
                    self.position += 4
                elif (5 == oc):
                    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
                    # Otherwise, it does nothing.
                    if 0 != av:
                        self.position = bv
                        if self.debug: print("{} OPCODE 5, setting pointer position to {}".format(self.name,bv))
                    else:
                        if self.debug: print("{} OPCODE 5, failed, skipping 3 pointer positions".format(self.name) )
                        self.position += 3
                elif (6 == oc):
                    #    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
                    # Otherwise, it does nothing.
                    if 0 == av:
                        self.position = bv
                        if self.debug: print("{} OPCODE 6, 0==av so moving it to {}".format(self.name,bv))
                    else:
                        if self.debug: print("{} OPCODE 6, 0!=av so skipping 3 ahead on the pointer".format(self.name))
                        self.position += 3
                elif (7 == oc):
                    if self.debug: print("{} OPCODE 7".format(self.name))
                    #    Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
                    # Otherwise, it stores 0.
                    if av < bv:
                        self.mydata[p] = 1
                        self.position += 4
                    else:
                        self.mydata[p] = 0
                        self.position += 4
                elif (8 == oc):
                    if self.debug: print("{}OPCODE 8 {}=?={}".format(self.name,av,bv))
                    #    Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
                    # Otherwise, it stores 0.
                    if av == bv:
                        self.mydata[p] = 1
                        self.position += 4
                    else:
                        self.mydata[p] = 0
                        self.position += 4
                else:
                    self.position += 1 # just skip the bad letter, probably a bad move, but I thought I read it once 



def resetdata():
    return [ 3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5] # test data, answer 139629729 from 9,8,7,6,5
    return [ 3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10] # 18216 from 9,7,8,5,6
    return [3,8,1001,8,10,8,105,1,0,0,21,30,51,72,81,94,175,256,337,418,99999,3,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1002,9,4,9,101,4,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]
    #ans = []
    #prog = open('advent07p2a.txt').readlines()
    #for a in prog[0].split(","):
    #    ans.append(int(a))
    #return ans

def combos():
    listA = [5,6,7,8,9]
    #perm = itertools.permutations(listA) 
    perm  = ([9, 8, 7, 5, 6],[9, 8, 7, 6, 5])
    maxthrust = 0
    eo = 0
    maxthrustcombo = []
    # del t1 when done
    mydata = resetdata()
    for i in list(perm): 
        # pass mydata, then an array of inputs from right to left (pop)
        #ao = processa(mydata,[0,i[0]]) # A
        # print("processed 0,{} ao={}".format(i[0],ao)) 
        # initially, but then they feed each other until it stops, and eo is good again
        print ("I={}".format(i))
        # print("ta=amplifier(mydata,{},A".format([0,i[0]]))
        ta = amplifier(mydata,[0,i[0]],"A") # A
        ta.debug = 1
        while (0 == len(ta.output)):
            ta.go()
        print("got an output from a: {}".format(ta.output[-1]))
        # print("tb=amplifier(mydata,{}...".format([ta.output,i[1]]))
        tb = amplifier(mydata,[ta.output.pop(),i[1]],"B") # B)
        tb.debug = 1
        while (0 == len(tb.output)):
            tb.go()
        # print("tc=amplifier(mydata,{}...".format([tb.output,i[2]]))
        tc = amplifier(mydata,[tb.output.pop(),i[2]],"C") # C)
        tc.debug = 1
        while (0 == len(tc.output)):
            tc.go()
        # print("td=amplifier(mydata,{},...".format([tc.output,i[3]]))
        td = amplifier(mydata,[tc.output.pop(),i[3]],"D") # D)
        td.debug = 1
        while (0 == len(td.output)):
            td.go()
        # print("te=amplifier(mydata,{}...".format([td.output,i[4]]))
        te = amplifier(mydata,[ td.output.pop(),i[4]],"E") # E)
        te.debug = 1
        while (0 == len(te.output)):
            te.go()
        ta.input.insert(0,te.output.pop())
        stillnewstuff = 1
        while (stillnewstuff):
            print("Running? a:{}, b:{}, c:{}, d:{}, e:{}".format(ta.runningstatus,tb.runningstatus,tc.runningstatus,td.runningstatus,te.runningstatus))
            print("Waiting? a:{}, b:{}, c:{}, d:{}, e:{}".format(ta.waitingoninput,tb.waitingoninput,tc.waitingoninput,td.waitingoninput,te.waitingoninput))
            ta.go()
            while (ta.output): tb.receiveinput(ta.output.pop())
            tb.go()
            while (tb.output): tc.receiveinput(tb.output.pop())
            tc.go()
            while (tc.output): td.receiveinput(tc.output.pop())
            td.go()
            while (td.output): te.receiveinput(td.output.pop())
            te.go()
            if (te.output):
                # print("te.output:{}".format(te.output[0]))
                eo = te.output.pop()
                ta.input.insert(0,eo)
            if not (ta.runningstatus or tb.runningstatus or tc.runningstatus or td.runningstatus or te.runningstatus):
                stillnewstuff = 0
        if eo > maxthrust:
            maxthrust = eo
            maxthrustcombo = i
        del ta, tb, tc, td, te

    print ("Max with {} is {}".format(maxthrust,maxthrustcombo))


if __name__ == "__main__":
    combos()
