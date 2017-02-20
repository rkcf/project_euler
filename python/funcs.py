""" Project Euler problems in python """

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
