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
