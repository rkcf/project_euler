""" Project Euler problems in python """

NOT_PRIMES = []

def is_prime(n, m):
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
            if is_prime(div, target):
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
