""" Project Euler problems in python """

NOT_PRIMES = []

def next_collatz(n):
    """Returns the next value in the collatz sequence starting with n"""
    if n % 2 == 0:
        return int(n/2)
    return 3 * n + 1

def find_factors(n):
    """Returns a list of the factors of n"""
    factors = []
    for i in range(1, int((n+2)/2)):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors

def gen_triangular(n):
    """Returns the triangular number made by summing the natural numbers 1 ... n"""
    return sum(range(1, n+1))

def is_prime_max(n, m):
    """ Returns True if number is a prime """
    if n in NOT_PRIMES:
        return False
    for x in range(2, int(n/2)):
        if n % x == 0:
            return False

    for i in range(2, m):
        if i > m/2:
            break
        NOT_PRIMES.append(i * n)

    return True

def is_prime(n):
    """Returns True if n is prime"""
    for x in range(2, int(n/2)+1):
        if n % x == 0:
            return False
    return True

def prime_sieve(m):
    """returns a list of all primes between 2 and m"""
    nums = list(range(2, m + 1))
    for n in nums:
        for i in range(2, m):
            p = i * n
            if p > m:
                break
            if p in nums:
                nums.remove(p)
    return nums

def problem1():
    """ Find the sum of all the multiples of 3 or 5 below 1000. """
    l = []
    for n in range(1000):
        if n % 3 == 0:
            l.append(n)
        elif n % 5 == 0:
            l.append(n)
    return sum(l)

def problem2():
    """ By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """
    fib = [1, 1]
    while True:
        new = fib[len(fib) - 1] + fib[len(fib) - 2]
        if new > 4000000:
            break
        else:
            fib.append(new)
    s = 0
    for n in fib:
        if n % 2 == 0:
            s += n

    return s

def problem3():
    """ What is the largest prime factor of the number 600851475143 ? """
    pfactors = []
    target = 600851475143
    for div in range(2, int(target/2)):
        if target % div == 0:
            if is_prime_max(div, target):
                pfactors.append(div)
    return max(pfactors)

def problem4():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    prods = [x * y for x in range(100, 1000) for  y in range(100, 1000)]
    palindromes = []
    for n in prods:
        reverse = []
        normal = list(str(n))
        for i in str(n):
            reverse.insert(0, i)
        if reverse == normal:
            palindromes.append(n)
    return max(palindromes)

def problem5():
    """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    for n in range(1, 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20):
        divisible = True
        for div in range(1, 21):
            if n % div != 0:
                divisible = False
                break
        if divisible:
            return n

def problem6():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
    squares = sum([x ** 2 for x in range(1, 101)])
    sumsquare = sum(range(1, 101)) ** 2
    diff = sumsquare - squares
    return diff

def problem7():
    """What is the 10001st prime number?"""
    i = 0
    n = 2
    while i != 10001:
        if is_prime(n):
            i += 1
        n += 1
    return n-1

def problem8():
    """Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"""
    num = ('73167176531330624919225119674426574742355349194934'
    '96983520312774506326239578318016984801869478851843'
    '85861560789112949495459501737958331952853208805511'
    '12540698747158523863050715693290963295227443043557'
    '66896648950445244523161731856403098711121722383113'
    '62229893423380308135336276614282806444486645238749'
    '30358907296290491560440772390713810515859307960866'
    '70172427121883998797908792274921901699720888093776'
    '65727333001053367881220235421809751254540594752243'
    '52584907711670556013604839586446706324415722155397'
    '53697817977846174064955149290862569321978468622482'
    '83972241375657056057490261407972968652414535100474'
    '82166370484403199890008895243450658541227588666881'
    '16427171479924442928230863465674813919123162824586'
    '17866458359124566529476545682848912883142607690042'
    '24219022671055626321111109370544217506941658960408'
    '07198403850962455444362981230987879927244284909188'
    '84580156166097919133875499200524063689912560717606'
    '05886116467109405077541002256983155200055935729725'
    '71636269561882670428252483600823257530420752963450')

    products = []
    for i in range(0, len(num) - 14):
        prod = 1
        for n in range(0, 13):
            prod = int(num[i + n]) * prod
        products.append(prod)

    return max(products)

def problem9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc."""
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        return a * b * c

def problem10():
    """Find the sum of all the primes below two million."""
    primes = prime_sieve(2000000)
    return sum(primes)

def problem11():
    """What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""
    grid = ('08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 '
            '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 '
            '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 '
            '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 '
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 '
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 '
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 '
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 '
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 '
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 '
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 '
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 '
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 '
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 '
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 '
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 '
            '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 '
            '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 '
            '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 '
            '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48')

    #put values into a tuple which defines their position, (value, x, y)
    grid_list = grid.split(' ')
    positions = []
    for y_pos in range(0, 20):
        for x_pos in range(0, 20):
            positions.append({'value':int(grid_list[x_pos + (y_pos * 20)]), 'x':x_pos, 'y':y_pos})

    products = []
    for pos in positions:
        #check up
        vals = [pos['value']]
        for i in range(1, 4):
            new_y = pos['y'] - i
            if new_y < 0:
                break
            for new_pos in positions:
                if new_pos['y'] == new_y and new_pos['x'] == pos['x']:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check down
        vals = [pos['value']]
        for i in range(1, 4):
            new_y = pos['y'] + i
            if new_y > 19:
                break
            for new_pos in positions:
                if new_pos['y'] == new_y and new_pos['x'] == pos['x']:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check left
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] - i
            if new_x < 0:
                break
            for new_pos in positions:
                if new_pos['y'] == pos['y'] and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check right
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] + i
            if new_x > 19:
                break
            for new_pos in positions:
                if new_pos['y'] == pos['y'] and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check upleft diag
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] + i
            new_y = pos['y'] - i
            if new_x > 19 or new_y < 0:
                break
            for new_pos in positions:
                if new_pos['y'] == new_x and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check upright diag
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] + i
            new_y = pos['y'] - i
            if new_x > 19 or new_y < 0:
                break
            for new_pos in positions:
                if new_pos['y'] == new_x and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check downleft diag
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] - i
            new_y = pos['y'] + i
            if new_x < 0 or new_y > 19:
                break
            for new_pos in positions:
                if new_pos['y'] == new_y and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

        #check downright diag
        vals = [pos['value']]
        for i in range(1, 4):
            new_x = pos['x'] + i
            new_y = pos['y'] + i
            if new_x > 19 or new_y > 19:
                break
            for new_pos in positions:
                if new_pos['y'] == new_x and new_pos['x'] == new_x:
                    vals.append(new_pos['value'])
        if len(vals) == 4:
            product = 1
            for i in range(0, 4):
                product *= vals[i]
            products.append(product)

    return max(products)

def problem12():
    """What is the value of the first triangle number to have over five hundred divisors?"""
    i = 1
    runningsum = 0
    while True:
        runningsum += i
        factors = find_factors(runningsum)
        if len(factors) > 500:
            return runningsum
        i += 1

def problem13():
    """Work out the first ten digits of the sum of the following one-hundred 50-digit numbers."""
    nums = [37107287533902102798797998220837590246510135740250
            , 46376937677490009712648124896970078050417018260538
            , 74324986199524741059474233309513058123726617309629
            , 91942213363574161572522430563301811072406154908250
            , 23067588207539346171171980310421047513778063246676
            , 89261670696623633820136378418383684178734361726757
            , 28112879812849979408065481931592621691275889832738
            , 44274228917432520321923589422876796487670272189318
            , 47451445736001306439091167216856844588711603153276
            , 70386486105843025439939619828917593665686757934951
            , 62176457141856560629502157223196586755079324193331
            , 64906352462741904929101432445813822663347944758178
            , 92575867718337217661963751590579239728245598838407
            , 58203565325359399008402633568948830189458628227828
            , 80181199384826282014278194139940567587151170094390
            , 35398664372827112653829987240784473053190104293586
            , 86515506006295864861532075273371959191420517255829
            , 71693888707715466499115593487603532921714970056938
            , 54370070576826684624621495650076471787294438377604
            , 53282654108756828443191190634694037855217779295145
            , 36123272525000296071075082563815656710885258350721
            , 45876576172410976447339110607218265236877223636045
            , 17423706905851860660448207621209813287860733969412
            , 81142660418086830619328460811191061556940512689692
            , 51934325451728388641918047049293215058642563049483
            , 62467221648435076201727918039944693004732956340691
            , 15732444386908125794514089057706229429197107928209
            , 55037687525678773091862540744969844508330393682126
            , 18336384825330154686196124348767681297534375946515
            , 80386287592878490201521685554828717201219257766954
            , 78182833757993103614740356856449095527097864797581
            , 16726320100436897842553539920931837441497806860984
            , 48403098129077791799088218795327364475675590848030
            , 87086987551392711854517078544161852424320693150332
            , 59959406895756536782107074926966537676326235447210
            , 69793950679652694742597709739166693763042633987085
            , 41052684708299085211399427365734116182760315001271
            , 65378607361501080857009149939512557028198746004375
            , 35829035317434717326932123578154982629742552737307
            , 94953759765105305946966067683156574377167401875275
            , 88902802571733229619176668713819931811048770190271
            , 25267680276078003013678680992525463401061632866526
            , 36270218540497705585629946580636237993140746255962
            , 24074486908231174977792365466257246923322810917141
            , 91430288197103288597806669760892938638285025333403
            , 34413065578016127815921815005561868836468420090470
            , 23053081172816430487623791969842487255036638784583
            , 11487696932154902810424020138335124462181441773470
            , 63783299490636259666498587618221225225512486764533
            , 67720186971698544312419572409913959008952310058822
            , 95548255300263520781532296796249481641953868218774
            , 76085327132285723110424803456124867697064507995236
            , 37774242535411291684276865538926205024910326572967
            , 23701913275725675285653248258265463092207058596522
            , 29798860272258331913126375147341994889534765745501
            , 18495701454879288984856827726077713721403798879715
            , 38298203783031473527721580348144513491373226651381
            , 34829543829199918180278916522431027392251122869539
            , 40957953066405232632538044100059654939159879593635
            , 29746152185502371307642255121183693803580388584903
            , 41698116222072977186158236678424689157993532961922
            , 62467957194401269043877107275048102390895523597457
            , 23189706772547915061505504953922979530901129967519
            , 86188088225875314529584099251203829009407770775672
            , 11306739708304724483816533873502340845647058077308
            , 82959174767140363198008187129011875491310547126581
            , 97623331044818386269515456334926366572897563400500
            , 42846280183517070527831839425882145521227251250327
            , 55121603546981200581762165212827652751691296897789
            , 32238195734329339946437501907836945765883352399886
            , 75506164965184775180738168837861091527357929701337
            , 62177842752192623401942399639168044983993173312731
            , 32924185707147349566916674687634660915035914677504
            , 99518671430235219628894890102423325116913619626622
            , 73267460800591547471830798392868535206946944540724
            , 76841822524674417161514036427982273348055556214818
            , 97142617910342598647204516893989422179826088076852
            , 87783646182799346313767754307809363333018982642090
            , 10848802521674670883215120185883543223812876952786
            , 71329612474782464538636993009049310363619763878039
            , 62184073572399794223406235393808339651327408011116
            , 66627891981488087797941876876144230030984490851411
            , 60661826293682836764744779239180335110989069790714
            , 85786944089552990653640447425576083659976645795096
            , 66024396409905389607120198219976047599490197230297
            , 64913982680032973156037120041377903785566085089252
            , 16730939319872750275468906903707539413042652315011
            , 94809377245048795150954100921645863754710598436791
            , 78639167021187492431995700641917969777599028300699
            , 15368713711936614952811305876380278410754449733078
            , 40789923115535562561142322423255033685442488917353
            , 44889911501440648020369068063960672322193204149535
            , 41503128880339536053299340368006977710650566631954
            , 81234880673210146739058568557934581403627822703280
            , 82616570773948327592232845941706525094512325230608
            , 22918802058777319719839450180888072429661980811197
            , 77158542502016545090413245809786882778948721859617
            , 72107838435069186155435662884062257473692284509516
            , 20849603980134001723930671666823555245252804609722
            , 53503534226472524250874054075591789781264330331690]

    return int(str(sum(nums))[0:10])

def problem14():
    """Given all collatz sequences, with starting number < 1000000, which produces the longest sequence"""
    sequences = []
    for i in range(1, 1000000):
        collatz = [i]
        n = i
        while collatz[len(collatz)-1] != 1:
            n = next_collatz(n)
            collatz.append(n)
        sequences.append((i, collatz))

    longest = (1, [1])
    for seq in sequences:
        if len(seq[1]) > len(longest[1]):
            longest = seq

    return longest[0]

def down(coordinates, m):
    """Returns the coordinates of the space one down"""
    new_y = coordinates[1] + 1
    if new_y >= m:
        return None
    return (coordinates[0], new_y)

def right(coordinates, m):
    """Returns the coordinates of the space one right"""
    new_x = coordinates[0] + 1
    if new_x >= m:
        return None
    return (new_x, coordinates[1])

class Route:
    """Class for a route through a cartesian grid system"""

    def __init__(self, positions):
        self.route = positions

    def last_pos(self):
        """returns last position of route"""
        return self.route[len(self.route) - 1]

    def next_pos(self, position):
        """appends position to end of route"""
        self.route.append(position)

def problem15():
    """Moving only right and down, starting from the top left corner, how many routes are there to the bottom right corner in a 20x20 grid"""
    start = Route([(0, 0)])
    routes = [start]
    terminated = []
    while routes:
        for r in routes:
            #print("working on route: " + str(r.route))
            print(r.route)
            new_pos = right(r.last_pos(), 20)
            if new_pos:
                new_r = Route(r.route)
                new_r.next_pos(new_pos)
                #print("created new route: " + str(new_r.route))
                if new_pos == (19, 19):
                    terminated.append(new_r)
                else:
                    routes.append(new_r)
            new_pos = down(r.last_pos(), 20)
            print(r.route)
            if new_pos:
                new_r = Route(r.route)
                new_r.next_pos(new_pos)
                if new_pos == (19, 19):
                    terminated.append(new_r)
                else:
                    routes.append(new_r)
            print(r.route) 
            routes.remove(r)
            print("total unfinished routes: " + str(len(routes)))
            #print("total finished routes: " + str(len(terminated)))

    return len(terminated)
