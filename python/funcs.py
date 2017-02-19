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
