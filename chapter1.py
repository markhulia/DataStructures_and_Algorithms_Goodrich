
import struct
#R-1.2
'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''
import re
import string
from collections import Counter
from random import choice, randrange, randint
import random


def isEven(m):
    if (-1) ** m == 1:
        print((-1)**m)
        return True
    return False


#R-1.3
'''Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.'''
def minmax(data):
    min = max = badVal = data[0]
    try:
        for i in range(len(data)):
            if data[i] <= min:
                min = data[i]
            elif data[i]>=max:
                max = data[i]
            elif not isinstance(data[i] ,int):
                pass
    except:
        print('bad values found at index:', i)
    return min, max


#R-1.4
'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.'''
def sqrsums(n):
    if n>0:
        sum = 0
        for i in range(n+1):
            sum += i**2
        return sum
    return False



#R-1.5
'''Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.'''
def sqrsums2(n):
    return sum([i**2 for i in range(n+1)])

#R-1.6, R-1.7
'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''
def sqrOddsums(n):
    return sum([i**2 for i in range(n+1) if i%2!=0])

#R-1.11
'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''
# print([2**n for n in range(9)])


#R-1.12
''' Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.'''
# from random import randrange
# print(randrange(10))


# C-1.15
def ints():
    l = []
    n = input('Enter a number: ("Enter" to quit): ')
    while n!='':
        try:
            if isinstance(int(n), int):
                l.append(int(n))
            n = input('Enter a number: ("Enter" to quit): ')
        except:
            print('not a number')
            break

    print(l)
# C-1.15
'''Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.'''
def odds(l):
    for i in range(len(l)):
        for n in range(i+1, len(l)):
            if ((l[i]*l[n])%2!=0)\
                    and (l[i]!=l[n]):
                yield l[i], l[n]

# for i in odds([1,2,3,3,4,5,6]):
#     print(i)


# C-1.18
'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].'''
# print([(x*(x-1)) for x in range(1,11)])

# C-1.19
''' Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally. '''
# print([chr(x) for x in range(97, 123)])


# C-1.20
'''Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.'''
def shuffle(l):
    for i in range(len(l)):
        r = randint(i, len(l)-1)
        l[i], l[r] = l[r], l[i]
    print('\n',l)


# C-1.21
'''Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).'''
def reader():
    l = []
    try:
        while EOFError:
             l.append(input('enter line: '))

    except EOFError:
        for i in range(len(l)):
            print(l[((len(l)-1)-i)])



# C-1.22
'''Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.'''
def dot_product(l1, l2):
    # assuming both lists are of an equal length
    dot = []
    for i in range(len(l1)):
        dot.append(l1[i]*l2[i])
    print(dot)


# C-1.23
'''Give an example of a Python code fragment that attempts to write an element
to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:'''
def overflow(l):
    try:
        l[len(l)] = 'new element'
    except (IndexError):
        print('“Don’t try buffer overflow attacks in Python!”')


# C-1.24
'''Write a short Python function that counts the number of vowels in a given
character string.'''
def vowels(s):
    count=0
    for i in s:
        if i in 'aeiou':
            count+=1
    print(count)

# C-1.25
'''Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let s try, Mike.", this function would return
"Lets try Mike".'''
def punctuation(s):
    return re.sub('[%s]' % re.escape(string.punctuation), '', s)


# C-1.26
'''Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”'''
def formula():
    try:
        a, b, c = eval(input('Enter three numbers separated by coma: '))
    except:
        print('srsly?')
        formula()
    if c == a+b or a == b-c or c==a*b:
        return True
    return False


# C-1.27
'''In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.'''
def factors(n):
    k = 1
    bigs =[]
    while k*k<n:
        if n % k == 0:
            yield k
            bigs.append(n // k)
        k += 1
    if k*k == n:
        yield k
    bigs.reverse()
    for n in bigs:
        yield n

# for i in factors(100):
#     print(i)



# P-1.29
'''Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.'''
def all_strings(str, iteration=0):
    if iteration == len(str):
        print(''.join(str))

    for i in range(iteration, len(str)):
        str_copy = [char for char in str]
        str_copy[i], str_copy[iteration] = str_copy[iteration], str_copy[i]
        all_strings(str_copy, iteration+1)





# P-1.30
'''Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.'''

def inStr():
    n = -1
    while n<2:
        try:
            n = int(input('Enter a positive integer greater than 2: '))
        except:
            pass
    print(positive(n))


def positive(n, step=0):
    if n < 2:
        # print(step)
        return step
    return positive(n//2, step+1)

# inStr()

# P-1.32
'''Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.'''
def simplecalc():
    # simple calculator assumes every input on a new line
    l = ''
    symbol = input()
    while symbol!='=':
        if symbol not in '=*/.+-()':
            if not isinstance(int(symbol), int):
                print('wrong symbol')
        l+=symbol
        symbol=input()
    print(eval(l))


# P-1.34
'''A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.'''
#return random indices for sentences which will be mistyped
def charIndex(sentence):
    return randrange(0, len(sentence))

#return random char indices in the sentence which will be mistyped
def sentenceIndex(rng):
    return random.sample(range(0, rng),8) #returns UNIQUE random numbers in the list

def typo(sentence):
    sentenceIndices = sorted(sentenceIndex(100))
    sl = 0
    for n in range(0, 100):
        if sl<=7 and sentenceIndices[sl]==n:
            print(n+1,sentence.replace(sentence[charIndex(sentence)],
                                   chr(randrange(97, 123)),1)) #replace char with random char
            sl+=1
        else:
            print(n+1, sentence)

# typo('I will never spam my friends again.')

# P-1.35
'''The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.'''

#generate random birthday dates (month, day)
def randomDate():
    month = randrange(1,13)
    if month in [1,3,5,7,8,10,12]:
        day = randrange(1,32)
    elif month in [4,6,9,11]:
        day = randrange(1,31)
    else:
        day = randrange(1,29)
    return month, day


def bdparadox(n, match = 0):
    for i in range(1,n):
        bd1 = randomDate()
        for b in range (2, n):
            bd2 = randomDate()
            if bd1 == bd2:
                match+=1
    return n, match, match/n     #return number of trials, duplicats found
                                 # and probability for current trial

def stats():
    l=[]
    for n in range(5, 101, 5):
        l.append(bdparadox(n))
    printStats(l)


def printStats(tpl):
    print('Trials:\tMatches:\tProbability')
    for i in tpl:
        print(' ',i[0],'    ',i[1],'        ',i[2])
stats()