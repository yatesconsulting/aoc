#!/usr/bin/python -Wall

class Card():
    ''' 5x5 bingo card with something in each space
    called numbers are replaced with X '''
    def __init__(self, gridvals, name=""):
        self.card = []
        self.name = name
        for i in gridvals:
            self.card.append(int(i)) 
        self.winner = False
    
    def __str__(self):
        nl = "\n"
        ans = self.name
        if self.winner:
            ans += " WINNER\n"
        else:
            ans += "\n"
        for x in range(5):
            a = self.card[5*x]
            b = self.card[5*x+1]
            c = self.card[5*x+2]
            d = self.card[5*x+3]
            e = self.card[5*x+4]
            if x == 4:
                nl = "\n" # remove if you don't want trailing newline, I found it handy
            ans += "{:>3}{:>3}{:>3}{:>3}{:>3}{}".format(a,b,c,d,e,nl)
        return ans

    def _inrow(self, row):
        if row < 5:
            return [0, 1, 2, 3, 4]
        elif row in [5,6,7,8,9]:
            return [5,6,7,8,9]
        elif row in [10,11,12,13,14]:
            return [10,11,12,13,14]
        elif row in [15,16,17,18,19]:
            return [15,16,17,18,19]
        elif row >19:
            return [20,21,22,23,24]

    def _incol(self, i):
        return [[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]][i % 5]
        
    def dob(self, num):
        if num in self.card:
            for key, value in enumerate(self.card):
                if value == num:
                    self.card[key] = "x"
                    self.winner = [self.card[a] for a in self._inrow(key)].count("x") == 5 or [self.card[a] for a in self._incol(key)].count("x") == 5

    def countupleftovers(self):
        cnt = 0
        for a in self.card:
            if a != 'x':
                cnt += int(a)
        return cnt

f = open("04inp.txt", "r")
# f = open("test.txt", "r", newline=None)
all=[]

line=a=b=b1=0
cards = []
cardsindex = 0
onecard = []
for l in f:
    l = l.strip()
    if line==0:
        numlist = l
    else:
        if l == "" and onecard:
            # print('line {} is blank and onecard has value'.format(line))
            cards.append(onecard)
            onecard = []
        else:
            # print('line {} is in else'.format(line))
            for a in l.split():
                onecard.append(a)
            # print ("onecard:{}".format(onecard))
    line += 1
cards.append(onecard) # lastcard has no newline after it

rcard = []
for i,card in enumerate(cards):
    rcard.append(Card(card,"Card {}".format(i+1)))

# ## ok, now for some real logic, Part 1
# # print('rcards: {}'.format(rcard))
# bingo = False
# for n in [int(a) for a in numlist.split(',')]:
#     # print("Calling out number {} (type {})".format(n, type(n)))
#     if not bingo:
#         for cnum,c in enumerate(rcard):
#             # if cnum < 2:
#                 # continue
#             # print(c.card)
#             c.dob(n)
#             # print ("card num {}\n{}".format(cnum, str(c)))
#             if c.winner:
#                 print("BINGO: card: {}".format(cnum))
#                 print ("card {}".format(str(c)))
#                 leftovers = c.countupleftovers()
#                 print("ans = winning number {} * leftovers {} = {}".format(n, leftovers, int(n)*leftovers))
#                 bingo = True
#                 break


# part 2

allbingosbutone = False
delme = []
for n in [int(a) for a in numlist.split(',')]:
    if rcard:
        # print("Calling out number {}".format(n))
        if delme:
            for c in sorted(delme, reverse=True):
                del rcard[c]
            delme = []
        for cnum,c in enumerate(rcard):
            c.dob(n)
            # print(str(c))
            if c.winner:
                if len(rcard) == 1:
                    # print ("BINGO on last card:\n{}".format(str(c)))
                    leftovers = c.countupleftovers()
                    print("ans = winning number {} * leftovers {} = {}".format(n, leftovers, n*leftovers))
                delme.append(cnum)

                
    # blah = input("Enter:")





f.close() 
