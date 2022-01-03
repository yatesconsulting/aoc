def process2():
    total = 0

    data = open("08inp.txt", "r")

    for line in data:
        s = line.split('|')
        v = s[0].replace('\n', ' ').strip().split(' ')
        f = s[1].replace('\n', ' ').strip().split(' ')

        one = ''.join(list(filter(lambda x: len(x) == 2, v))[0])
        four = ''.join(list(filter(lambda x: len(x) == 4, v))[0])
        seven = ''.join(list(filter(lambda x: len(x) == 3, v))[0])
        eight = ''.join(list(filter(lambda x: len(x) == 7, v))[0])

        one = ''.join(sorted(one))
        four = ''.join(sorted(four))
        seven = ''.join(sorted(seven))
        eight = ''.join(sorted(eight))

        top = set(seven) - set(one)

        two_three_five = [''.join(sorted(i)) for i in list(filter(lambda x: len(x) == 5, v))]

        three = ''.join(sorted(list(filter(lambda x: one[0] in x and one[1] in x, two_three_five))[0]))

        bottom = set(three) - set(four) - top

        nine = ''.join(sorted(list(set(four).union(top).union(bottom))))

        bottom_left = set(eight) - set(nine)

        two_three_five.remove(three)

        two = ''.join(sorted(list(filter(lambda x: list(bottom_left)[0] in x, two_three_five))[0]))

        two_three_five.remove(two)

        five = two_three_five[0]

        top_left = list(set(five) - set(two) - set(one))[0]

        middle = set(four) - set(top_left) - set(one)

        zero = ''.join(sorted(list(set(eight) - middle)))

        six = ''.join(sorted(list(set(five).union(bottom_left))))

        ref = {
                zero: 0,
                one: 1,
                two: 2,
                three: 3,
                four: 4,
                five: 5,
                six: 6,
                seven: 7,
                eight: 8,
                nine: 9,
                }

        out = ''

        for val in f:
            val = ''.join(sorted(val))

            out += str(ref.get(val))

        total += int(out)

    print(total)

process2()
