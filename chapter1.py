'''Write a short Python function, is multiple(n, m), that takes two
integer values and returns True if n is a multiple of m, that is,
n = mi for some integer i, and False otherwise.'''

# R-1.1
import string
from random import randint, randrange

from math import factorial


def is_multiple(N, M):
    if M%N == 0:
        return True
    return False


# R-1.2


# R-1.3
'''Write a short Python function, minmax(data), that takes a sequence
of one or more numbers, and returns the smallest and largest numbers,
in the form of a tuple of length two. Do not use the built-in functions
 min or max in implementing your solution.'''
def minmax(data):
    data.sort()
    return (data[0],data[-1])


# R-1.4
'''Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller
 than n.'''
def square_sums(N):
    sum=0
    for i in range(N):
        sum+=i*i
    return sum


# R-1.5
'''Give a single command that computes the sum from Exercise R-1.4,
 relying on Python’s comprehension syntax and the built-in
 sum function.'''
def square_sums_comprehension(N):
    return sum([i*i for i in range(N)])


# R-1.6
'''Write a short Python function that takes a positive integer n
 and returns the sum of the squares of all the odd positive
 integers smaller than n.'''
def odd_squares(N):
    return sum([i*i for i in range(N) if i % 2 != 0])


# C-1.14
'''Write a short Python function that takes a sequence of integer
 values and determines if there is a distinct pair of numbers in
 the sequence whose product is odd.'''
def odd_products(L):
    lst = []
    for i in range(len(L)):
        if (L[i] % 2 != 0) and L[i] not in lst:
            lst.append(L[i])
    if len(lst)>2:
        return L[0], L[1] #just return first two elements
    return False


# C-1.15
'''Write a Python function that takes a sequence of numbers and
determines if all the numbers are different from each other
 (that is, they are distinct).'''
def distinct_numbers(L):
    temp = []
    for i in range(len(L)):
        if L[i] not in temp:
            temp.append(L[i])
        else:
            return False
    if len(L)!=len(temp):
        return False
    return True


# C-1.18
'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].'''
# [i*(i-1) for i in range(1,10)]


# C-1.19
'''Demonstrate how to use Python’s list comprehension syntax to produce
thelist[ a , b , c ,..., z ],butwithouthavingtotypeall26such characters
literally.'''
# [chr(i) for i in range(97, 123)]


# C-1.20
'''Python’s random module includes a function shuffle(data) that accepts
a list of elements and randomly reorders the elements so that each
possible order occurs with equal probability. The random module includes
a more basic function randint(a, b) that returns a uniformly random
integer from a to b (including both endpoints). Using only the randint
function, implement your own version of the shuffle function.'''
def _shuffle(L):
    # shuffled = [None] * len(L)
    # for i in range(len(shuffled)):
    #     shuffled[i] = L.pop(randint(0, (len(L)-1)))
    # return shuffled
    for i in range(len(L)):
        rand = L[randint(i, (len(L)-1))]
        L[i],  L[rand]= L[rand], L[i]
    return L


# C-1.21
'''Remove punctuation for the string'''
def remove_punctuation(S):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in S if ch not in exclude)


# C-1.27
'''In Section 1.8, we provided three different implementations of a
generator that computes factors of a given integer. The third of those
implementations, from page 41, was the most efficient, but we noted
that it did not yield the factors in increasing order. Modify the
generator so that it reports factors in increasing order,
while maintaining its general performance advantages.'''

def factors(n):
    k=1
    c = -1
    bigs = []
    while k*k<n:
        if n%k==0:
            yield k
            bigs.append(n//k)
        k+=1
    if k*k == n:
        yield k
    for i in range(len(bigs)):
        yield bigs[c]
        c -= 1


# P-1.29
'''Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o ,and g exactly once.'''
def string_formatinon(S, iteration = 0):
    if iteration==len(S):
        print(''.join(S))

    for i in range(iteration, len(S)):
        S_copy = [ch for ch in S]
        S_copy[i], S_copy[iteration] = S_copy[iteration], S_copy[i]
        string_formatinon(S_copy, iteration+1)


# P-1.30
'''Write a Python program that can take a positive integer greater
than 2 as input and write out the number of times one must
repeatedly divide this number by 2 before getting a value less
than 2.'''
def divide_by2(N):
    step = 0
    while N>1:
        N /= 2
        step += 1
    return step


# P-1.32
'''Write a Python program that can simulate a simple calculator,
using the console as the exclusive input and output device.
That is, each input to the calculator, be it a number,
like 12.34 or 1034, or an operator, like + or =, can be
done on a separate line. After each such input, you should
output to the Python console what would be displayed on your
calculator.'''
def calculator():
    screen = ''
    symbol = input()
    while symbol!='=':
        if symbol not in '+-*/()':
            try:
                isinstance(int(symbol), int)
            except:
                return 'Wrong Symbol'
        screen+=symbol
        symbol=input()
    return eval(screen)


# P-1.34
'''A common punishment for school children is to write out a
sentence multiple times. Write a Python stand-alone program
that will write out the following sentence one hundred
times: “I will never spam my friends again.” Your program
should number each of the sentences and it should make eight
different random-looking typos.'''
def typos(sentence):
    random_sentences = [randint(1,100) for _ in range(8)]
    random_sentences.sort()
    # print(random_sentences)
    for i in range(100):
        if random_sentences != []:
            if i == random_sentences[0]:
                print('typo>>>',sentence.replace(sentence[randint(0, len(sentence))],
                                       chr(randint(97,122)),1))
                random_sentences.pop(0)

        print((i+1),(sentence))



# P-1.35
'''The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.'''
def birthday_paradox():
    # generate list of lists with random birthday dates
    birthdays = [[randint(1,365) for i in range(n)]for n in range(5,101,5)]
    # dictionary for results with key=number of experiments and val=number of matched bdays
    results = {i:0 for i in range(5,101,5)}
    for i in birthdays:
        statistics = stats(i)
        results[len(i)]=[statistics, + statistics/len(i)]
    return results


def stats(L):
    bdays = []
    match = 0
    for i in L:
        if i in bdays:
            match+=1
        bdays.append(i)
    return match










