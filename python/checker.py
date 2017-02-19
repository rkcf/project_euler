""" Checks project euler answers """

import csv
from sys import argv
import funcs

#get problem number argument from command line
assert len(argv) == 2, 'Please pass the problem number'
pnum = argv[1]

#open file
with open('../answers.csv', 'r') as answersCsv:
    answers = csv.reader(answersCsv, delimiter=',')
    for row in answers:
        if row[0] == pnum:
            ans = row[1]
            func = getattr(funcs, 'problem' + pnum)
            myans = func()
            if myans == int(ans):
                print("You have sucessfully solved problem " + pnum)
            else:
                print( "My answer: " + str(myans) + "\n" + "Try again.  Incorrect answer to problem " + pnum)
            break
