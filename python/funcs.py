""" Project Euler problems in python """

NOT_PRIMES = []

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
