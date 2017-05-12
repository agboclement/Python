# Q013
# Created by JKChang
# 28/02/2017, 11:29
# Tag: count digits and letters
# Description: Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Example: Suppose the following input is supplied to the program:
#          hello world! 123
#          Then, the output should be:
#          LETTERS 10
#          DIGITS 3

s = raw_input('please input sequence of text')
d = {'DIGITS': 0, 'LETTERS': 0}

for c in s:
    if c.isdigit():
        d['DIGITS'] += 1
    elif c.isalpha():
        d['LETTERS'] += 1
    else:
        pass

print "LETTERS: ", d['LETTERS']
print "DIGITS: ", d['DIGITS']