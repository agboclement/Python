# review
# Created by JKChang
# 12/05/2017, 14:10
# Tag:
# Description: use to review the practice



# ----------------Q001-----------------
# Description: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#              between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated
#              sequence on a single line.

# list = []
# for i in range (2000, 3000):
#     if i % 7 ==0 and i% 5!= 0:
#         list.append(str(i))
# print ','.join(list)

# ----------------Q002-----------------
# Description: Write a program which can compute the factorial of a given numbers.
#              The results should be printed in a comma-separated sequence on a single line.
#              Suppose the following input is supplied to the program:

# def fact(x):
#     if x ==0:
#         return 1
#     return fact(x-1) *x
#
# x = int(raw_input())
# print fact(x)

# ----------------Q003-----------------
# Description: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
#              that is an integral number between 1 and n (both included). and then the program should print the
#              dictionary.

# dict = {}
# n = int(raw_input())
# for x in range (1,n+1):
#     dict[x] = x * x
#
# print dict

# ----------------Q004-----------------
# Description: Write a program which accepts a sequence of comma-separated numbers from console and generate a list
#              and a tuple which contains every number.

# seq = '12,23,45,68,21,43,87'
# list = seq.split(',')
# print tuple(list)

# ----------------Q005-----------------
# # Description: Define a class which has at least two methods:
#                getString: to get a string from console input # printString: to print the string in upper case.
#                Also please include simple test function to test the class methods.

# class InOutString(object):
#     def __init__(self):
#         self.str = ''
#
#     def getString(self):
#         self.str = raw_input('input: ')
#
#     def printString(self):
#         print self.str.upper()
#
#
# test = InOutString()
# test.getString()
# test.printString()

# ----------------Q006-----------------
# Description: Write a program that calculates and prints the value according to the given formula:
#                       Q = Square root of [(2 * C * D)/H]
#              Following are the fixed values of C and H: C is 50. H is 30.
#              D is the variable whose values should be input to your program in a comma-separated sequence.

# import math
#
#
# def converter(d):
#     c = 50
#     h = 30
#     return int(round(math.sqrt(2 * c * float(d) / h)))
#
#
# items = [x for x in raw_input().split(',')]
# res = []
# for item in items:
#     res.append(str(converter(int(item))))
#
# print ','.join(res)

# ----------------Q007-----------------
# Description: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element
#              value in the i-th row and j-th column of the array should be i*j.
#              Note: i=0,1.., X-1; j=0,1 !=Y-1.

# dimennsions = [int(x) for x in raw_input('please input rowNum and colNum').split(',')]
# rowNum = dimennsions[0]
# colNum = dimennsions[1]
#
# resArray = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# for row in range(rowNum):
#     for col in range(colNum):
#         resArray[row][col] = row * col
#
# print resArray

# ----------------Q008-----------------
# Description: Write a program that accepts a comma separated sequence of words as input and prints the words in a
#              comma-separated sequence after sorting them alphabetically.

# seq = [ x for x in raw_input().split(',')]
# seq.sort()
# print ','.join(seq)

# ----------------Q009-----------------
# Description: Write a program that accepts sequence of lines as input and prints the lines after making all
#              characters in the sentence capitalized.

# line = []
# while True:
#     s = raw_input()
#     if s:
#         line.append(s.upper())
#     else:
#         break
#
# for p in line:
#     print p

# ----------------Q010-----------------
# Description: Write a program that accepts a sequence of whitespace separated words as input and prints the words
#              after removing all duplicate words and sorting them alphanumerically.

# li = [x for x in raw_input().split(' ')]
# li = sorted(list(set(li)))
# print ' '.join(li)

# ----------------Q011-----------------
# Description: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
#              then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
#              printed in a comma separated sequence.

# li = [x for x in raw_input().split(',')]
# res = []
#
# for x in li:
#     dec_x = int(x, 2)
#     if not dec_x % 5:
#         res.append(x)
# print ','.join(res)

# ----------------Q012-----------------
# Description: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
#              digit of the number is an even number. The numbers obtained should be printed in a comma-separated
#              sequence on a single line.

# res = []
# for i in range(1000, 3001):
#     s = str(i)
#     if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
#         res.append(s)
# print ','.join(res)

# ----------------Q013-----------------
# Description: Write a program that accepts a sentence and calculate the number of letters and digits.
# s = raw_input('please input sequence of text:')
# d = {'DIGITS': 0, 'LETTERS': 0}

# for char in s:
#     if char.isdigit():
#         d['DIGITS'] += 1
#     if char.isalpha():
#         d['LETTERS'] += 1
#     else:
#         pass
# print "LETTERS: ", d['LETTERS']
# print "DIGITS: ", d['DIGITS']

# ----------------Q014-----------------
# Description: Write a program that accepts a sentence and calculate the number of upper case letters and lower case
#              letters.

# s = raw_input()
# dict = {"LOWER": 0, "UPPER": 0}
#
# for char in s:
#     if char.islower():
#         dict['LOWER'] += 1
#     elif char.isupper():
#         dict['UPPER'] += 1
#     else:
#         pass
#
# print 'UPPER CASE:', dict['UPPER']
# print 'LOWER CASE:', dict['LOWER']

# ----------------Q015-----------------
# Description: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# a = str(raw_input())
# aa = int('%s%s' % (a, a))
# aaa = int('%s%s%s' % (a, a, a))
# aaaa = int('%s%s%s%s' % (a, a, a, a))
#
# print int(a) + aa + aaa + aaaa

# ----------------Q016-----------------
# Description: Use a list comprehension to square each odd number in a list. The list is input by a sequence of
#              comma-separated numbers.

# nums = [x for x in raw_input().split(',') if int(x)%2 != 0]
# print ','.join(nums)

# ----------------Q017-----------------
# Description: Write a program that computes the net amount of a bank account based a transaction log from console input.
#              The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.

# res = 0
#
# while True:
#     s = raw_input('D:deposit and W:withdrawal \n')
#     if not s:
#         break
#
#     value = s.split(' ')
#     operation = value[0]
#     amount = value[1]
#
#     if operation == 'D':
#         res += int(amount)
#     elif operation == 'W':
#         res -= int(amount)
#     else:
#         pass
#
# print res

# ----------------Q018-----------------
# Description: A website requires the users to input username and password to register. Write a program to check the
#              validity of password input by users.
#
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#     Passwords that match the criteria are to be printed, each separated by a comma.

# import re
#
# while True:
#     s = raw_input('Password: ')
#     if not s:
#         break
#
#     if not re.search('[a-z]', s):
#         print 'At least 1 letter between [a-z]'
#         continue
#
#     if not re.search('[0-9]', s):
#         print 'At least 1 number between [0-9]'
#         continue
#
#     if not re.search('[A-Z]', s):
#         print 'At least 1 letter between [A-Z]'
#         continue
#
#     if not re.search('[$#@]', s):
#         print 'At least 1 symbol in [$#@]'
#         continue
#
#     if len(s) < 6 or len(s) > 12:
#         print 'length should between 6 to 12 '
#         continue
#     else:
#         print "Well done! your password is: ", s
#         break

# ----------------Q019-----------------
# Description: You are required to write a program to sort the (name, age, height) tuples by ascending order where name
#              is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.

# from operator import itemgetter
#
# l = []
# while True:
#     s = raw_input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
#
# print sorted(l, key=itemgetter(0, 1, 2))


# ----------------Q020-----------------
# Description: Define a class with a generator which can iterate the numbers, which are divisible by 7,
#              between a given range 0 and n.
#
#     def Genert(n):
#         i = 0
#         while i < n:
#             j = i
#             i += 1
#             if j % 7 == 0:
#                 yield j
#
#     for i in Genert(100):
#         print i

# ----------------Q021-----------------
# Description: The numbers after the direction are steps. Please write a program to compute the distance from current
#              position after a sequence of movement and original point. If the distance is a float, then just print
#              the nearest integer.

#
# import math
#
# pos = [0, 0]
#
# while True:
#     s = raw_input()
#     if not s:
#         break
#
#     move = s.split(' ')
#     direction = move[0]
#     step = int(move[1])
#     if direction.upper() == 'UP':
#         pos[1] += step
#     elif direction.upper() == 'DOWN':
#         pos[1] -= step
#     elif direction.upper() == 'LEFT':
#         pos[0] += step
#     elif direction.upper() == 'RIGHT':
#         pos[0] -= step
#     else:
#         pass
#
#     print 'Distance: ', int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2)))

# ----------------Q022-----------------
# Description: Write a program to compute the frequency of the words from the input. The output should output after
#              sorting the key alphanumerically.

# import operator
#
# freq = {}
# line = raw_input()
#
# for word in line.split(" "):
#     freq[word] = freq.get(word, 0) + 1
#
# print 'dictionary: ', freq
# # sorted according to the term frequency (values)
# freq1 = sorted(freq.items(), key=operator.itemgetter(1))
# print type(freq1)
#
# print 'sorted according to the term frequency (values): ', freq1
#
# # sorted according to the alphabetical (keys)
# freq2 = sorted(freq.items(), key=operator.itemgetter(0))
# print 'sorted according to the alphabetical (keys) : ', freq2

# ----------------Q023-----------------
# Description: Write a method which can calculate square value of number
#
# def square(n):
#     return n**2
#
# n = int(raw_input())
# print square(n)

# ----------------Q024-----------------
# Description:  Python has many built-in functions, and if you do not know how to use it, you can read document online
#               or find some books. But Python has a built-in document function for every built-in functions.
#               Please write a program to print some Python built-in functions documents, such as abs(), int(),
#               raw_input() And add document for your own function

# def square(num):
#     '''return the square value'''
#     return num **2
#
# print square(3)
# print square.__doc__


# ----------------Q025-----------------
# Description:  Define a class, which have a class parameter and have a same instance parameter.
# class Person(object):
#     name = 'someone'
#
#     def __init__(self, n=None):
#         self.name = n
#
#
# dav = Person('David')
# print 'dav name:', dav.name
# print 'Person name: ', Person.name
#
# Person.name = 'Chan'
# print 'change Person name:', Person.name
#
# dove = Person('Dove')
# print 'dove name: ', dove.name
# print 'Person name: ', Person.name

# ----------------Q026-----------------
# Description: Define a function which can compute the sum of two numbers.
# def sum(num1, num2):
#     return num1+num2
#
# print sum(3,5)

# ----------------Q027-----------------
# Description: Define a function that can convert a integer into a string and print it in console.
# def convert(num):
#     return str(num)
#
# print convert(32)


# ----------------Q028-----------------
# Description: Define a function that can convert a string into a int and print it in console.
# def ConvertorStr(str):
#     return int(str)
#
# print ConvertorStr('11')


# ----------------Q029-----------------
# Description: Define a function that can receive two integral numbers in string form and compute their sum and then
#              print it in console.
#
# def sum(num1,num2):
#     return int(num1) + int(num2)
#
# print sum('2','5')

# ----------------Q030-----------------
# Description: Define a function that can accept two strings as input and concatenate them and then print it in console.
# def printV(s1,s2):
#     return s1+s2
#
# print printV('hello', 'world')


# ----------------Q031-----------------
# Description: Define a function that can accept two strings as input and print the string with maximum length in
#              console. If two strings have the same length, then the function should print all strings line by line.

# def printV(s1, s2):
#     if (len(s1) > len(s2)):
#         print s1
#     elif (len(s1) < len(s2)):
#         print s2
#     else:
#         print s1
#         print s2
#
# printV('information', 'retrieval')

# ----------------Q032-----------------
# Description: Define a function that can accept an integer number as input and print the "It is an even number" if
#              the number is even, otherwise print "It is an odd number".

# def checkValue(num):
#     if (num %2 ==0):
#         print '%d is an even num' %num
#     else:
#         print '%d is an odd num' %num
#
# checkValue(100)
# checkValue(101)

# ----------------Q033-----------------
# Description: Define a function which can print a dictionary where the keys are numbers between 1 and 3
# def creatDict(num):
#     d = {}
#     for i in range(1, num + 1):
#         d[i] = i ** 2
#     return d
#
#
# print creatDict(5)

# ----------------Q034-----------------

# Description: Define a function which can print a dictionary where the keys are numbers between 1 and 20
#              (both included) and the values are square of keys.

# d = creatDict(20)

# ----------------Q035-----------------
# Description: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both
#              included) and the values are square of keys. The function should just print the values only.

# for key in d.keys():
#     print d[key]

# ----------------Q036-----------------
# Description: Define a function which can generate a dictionary where the keys are numbers between 1 and 20
#              (both included) and the values are square of keys. The function should just print the keys only.
# d = creatDict(20)
# print d.keys()

# ----------------Q037-----------------
# Description: Define a function which can generate and print a list where the values are square of numbers
#              between 1 and 20 (both included).

# d = creatDict(20)
# li = []
#
# for key in d.keys():
#     li.append(d[key])
#
# print li

# ----------------Q038-----------------
# Description: Define a function which can generate a list where the values are square of numbers between 1 and 20 (
#              both included). Then the function needs to print the first 5 elements in the list.

# print li[:5]

# ----------------Q039-----------------
# Description: Define a function which can generate a list where the values are square of numbers between 1 and 20
#              (both included). Then the function needs to print the last 5 elements in the list.
# print li[-5:]

# ----------------Q040-----------------
# Description: Define a function which can generate a list where the values are square of numbers between 1 and 20
#              (both included). Then the function needs to print all values except the first 5 elements in the list.

# print li[5:]

# ----------------Q041-----------------
# Description: Define a function which can generate and print a tuple where the value are square of numbers between 1
#              and 20 (both included).
#
# print tuple(li)


# ----------------Q042-----------------
# Description: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
#              and the last half values in one line.



# ----------------Q043-----------------



# ----------------Q044-----------------



# ----------------Q045-----------------



# ----------------Q046-----------------



# ----------------Q047-----------------



# ----------------Q048-----------------



# ----------------Q049-----------------



# ----------------Q050-----------------



# ----------------Q051-----------------



# ----------------Q052-----------------



# ----------------Q053-----------------



# ----------------Q054-----------------



# ----------------Q055-----------------



# ----------------Q056-----------------



# ----------------Q057-----------------



# ----------------Q058-----------------



# ----------------Q059-----------------



# ----------------Q060-----------------



# ----------------Q061-----------------



# ----------------Q062-----------------



# ----------------Q063-----------------



# ----------------Q064-----------------



# ----------------Q065-----------------



# ----------------Q066-----------------



# ----------------Q067-----------------



# ----------------Q068-----------------



# ----------------Q069-----------------



# ----------------Q070-----------------



# ----------------Q071-----------------



# ----------------Q072-----------------



# ----------------Q073-----------------



# ----------------Q074-----------------



# ----------------Q075-----------------



# ----------------Q076-----------------



# ----------------Q077-----------------



# ----------------Q078-----------------



# ----------------Q079-----------------



# ----------------Q080-----------------



# ----------------Q081-----------------



# ----------------Q082-----------------



# ----------------Q083-----------------



# ----------------Q084-----------------



# ----------------Q085-----------------



# ----------------Q086-----------------



# ----------------Q087-----------------



# ----------------Q088-----------------



# ----------------Q089-----------------



# ----------------Q090-----------------



# ----------------Q091-----------------



# ----------------Q092-----------------



# ----------------Q093-----------------



# ----------------Q094-----------------



# ----------------Q095-----------------



# ----------------Q096-----------------



# ----------------Q097-----------------



# ----------------Q098-----------------



# ----------------Q099-----------------



# ----------------Q100-----------------