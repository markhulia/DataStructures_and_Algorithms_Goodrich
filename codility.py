from random import randrange
from time import time

import collections
from scipy._lib.six import xrange

import itertools




def solution(l):

    # print(list(enumerate(l)))
    suml, sumr, mid= 0, sum(l), 0

    for index, value in enumerate(l):
        suml += mid
        sumr -= value
        mid = value
        print('suml: {}, sumr: {})'.format(suml, sumr))
        if suml == sumr:
            return index

    return -1

def randoms():
    l = []
    for i in range(1000):
        l.append(randrange(-10,10))

    print(l)





def binary_gap(N):
    # write your code in Python 2.7
    nStr = str(bin(N)).strip("0b")
    print(nStr)
    count = 0
    l = []
    for i in nStr:
        if int(i) == 0:
            count+=1
        l.append(count)
        if int(i)!=0:
            count=0
    return(max(l))

# print(binary_gap(6))

def rotate(A, K):
    if A==[]:
        return A

    for i in range(K):
        # for n in xrange(len(A)):
        element = A.pop()
        A.append(A.insert(0, element))
        A.pop()
    return A

# print(rotate([3, 8, 9, 7, 6], 3))

def singles(A):
    # write your code in Python 2.7
    A = sorted(A)
    print(A)
    length = len(A)
    if length==1:
        return A[0]


    for i in range(0,length,2):
        try:
            if A[i]!=A[i+1]:
                return A[i]
        except:
            return A[i]
    return 0

    #amazingly fast solution
    # result = 0
    # for number in A:
    #     result ^= number
    #
    # return result
# print(singles([1,1,2,3,3]))

def frogjump(X, Y, D):
    jump = (Y-X) // D
    rem = (Y-X) % D
    if rem!=0:
        return jump+1
    return jump

# print(frogjump(10,85,30))

def tapeEquilibrium(A):
    l = []
    suml , sumr = 0, sum(A)
    for i in range(0,len(A)-1):
        suml += A[i]
        sumr -=A[i]
        l.append(abs(suml-sumr))
    return min(l)

# print(tapeEquilibrium([3, 1, 2, 4, 3]))


def permMissingElement(A):
    A = sorted(A)
    if A == []:
        return 1
    for i in range(1, len(A)):
        if A[i]-A[i-1]!=1:
            return A[i]-1
    if A[0]==2:
        return 1
    else: return A[-1]+1

# print(permMissingElement([1,3,4,5]))


#100%-40%
def frogRiverOne(X,A):
    # write your code in Python 2.7
    path = [0] * X
    for index, value in enumerate(A):
        # print path
        if 0 not in path:
            return index-1
        else:
            path[value-1] = value

    if 0 not in path:
        return index
    else:
        return -1

# print(frogRiverOne(5,[1,2,3,4,3,4,5]))


def permutation(A):
    A = sorted(A)
    if A[0]!=1:
        return 0

    for i in range(1,len(A)):
        if A[i]-A[i-1]!=1:
            return 0
    return 1

    #shorter solution:
    # A=sorted(A)
    # if A==range(1, len(A)+1):
    #     return 1
    # else: return - 1


# 100%-100%
def missingInteger(A):
    # write your code in Python 2.7
    l = len(A)
    A = frozenset(A)
    for i in range(1, l+1):
        if i not in A:
            return i
    return max(A)+1
# print(missingInteger([3,4,6,4,5,6,7,3])



# 100%-0% timeout error
def max_counters(N,A):
    l = len(A)
    ls = [0]*N

    for i in range(l):
        if A[i]<=N:
            ls[A[i]-1]+=1
        else:
            ls = [max(ls) for x in ls]

    return ls

# 100%-100%
def passingCars(A):
    total = east = 0

    for i in range(len(A)):
        if A[i]==0:
            east+=1
        elif A[i]==1:
            total+=east
    if total>1000000000:
        return -1
    return total
# print(passingCars([1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1]))



# 100%-0%
def countDiv(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i%K==0:
            count+=1
    return count

    # 100%-100%
    # edge = 1 if A%K == 0 else 0
    # return B//K - A//K + edge

# print(countDiv(4,10,3))





def geometricRangeQuery(S, P, Q):
    #100% - 0%
    A, C, G, T = 1, 2, 3, 4
    DNA = {'A':1, 'C':2, 'G':3, 'T':4}
    values = []
    result = []
    index = 0
    for i in range(len(P)):
        # print P[i]
        l = range(P[i], Q[i]+1)
        for val in range(len(l)):

            values.append(DNA[S[l[val]]])

        result.append(min(values))
        values = []
    return result

def triangle(A):
    # 100%- 50%
    # if len(A)<3:
    #     return 0
    # A = sorted([x for x in A if x>=0])
    # # print A
    # for i in range(len(A)-2):
    #     for n in range(i+1,len(A)-1):
    #         # if A[i]!=A[n]:
    #         for v in range(n+1,len(A)):
    #             if (A[i]+A[n]>A[v]) and (A[n]+A[v]>A[i]) and (A[i]+A[v]>A[n]):
    #                             # print('A[i]:{}; A[v]:{}; A[n]:{}'.format(A[i], A[v], A[n]))
    #                         return 1
    # return 0

    # 100%-100%
    A = sorted(A)
    for index in range(0, len(A)-2):
        if A[index]+A[index+1]>A[index+2]:
            return 1
    return 0

# print(triangle([1,1,2,3,4,5]))



def maxProductOfThree(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

# print(maxProductOfThree([-5,2,3,4,-1,-6, 2,8,3,1]))


def fish(A, B):
    # 75%-25%
    i = 1
    while i<len(A):
        # print('A-1',A[i-1], B[i-1])
        # print('A  ', A[i], B[i])
        # print
        if B[i-1] == 0:
            i+=1
            continue

        if A[i-1]>A[i]:
            if B[i-1]!=B[i]:
                # print('deleting1: ',A[i],B[i])
                del A[i], B[i]
                continue
        if A[i-1]<A[i]:
            if B[i-1]!=B[i]:
                # print('deleting2: ',A[i-1], B[i-1])
                del  A[i-1], B[i-1]
                continue

        i+=1
    # print A
    return len(A)


def fishes(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream

    for index in xrange(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1

    # Currently, all the downstream-flow fishs in stack
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)

    return alive_count


def nesting(S):
    # write your code in Python 2.7
    if len(S)%2!=0:
        return 0 #unbalanced string
    if S=='':
        return 1
    st = {')':'('}
    to_push = '('
    stack=[]
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack)==0:
                return 0
            elif st[element]!=stack.pop():
                return 0
    if len(stack)==0:
        return 1
    else: return 0

# print(nesting('(())'))

def goldenLeader(A):
    n = len(A)
    size=0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            count += 1
    if(count>n//2):
        leader = candidate
    return leader

# print(goldenLeader([1,2,1,3,1,4,1,5,1,6,1]))


def dominator(A):
    # write your code in Python 2.7
    l = len(A)
    size = 0
    for i in xrange(l):
        if size==0:
            size+=1
            value = A[i]
        else:
            if A[i]==value:
                size+=1
            else:
                size-=1
    candidate = -1
    count=0
    for i in xrange(l):
        if A[i]==value:
            count+=1
    if count>l//2:
        return A.index(value)
    else:
        return candidate



def equi_leader(A):
    l = len(A)
    size=0
    for i in xrange(l):
        if size==0:
            size+=1
            value = A[i]
        else:
            if A[i]==value:
                size+=1
            else:
                size-=1
    candidate = -1
    count=0
    for i in xrange(l):
        if A[i]==value:
            count+=1
    if count>l//2:
        candidate = value
    else:
        return 0

    equi_leaders = 0
    leader_count = 0
    for i in xrange(l):
        if A[i]==candidate:
            leader_count+=1
        if leader_count>(i+1)//2 and (count-leader_count) > (l-i-1)//2:
            equi_leaders+=1
    return equi_leaders


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_endng = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

# golden_max_slice([1,2,3,4,5,6,7])

def perimeter(N):
    # write your code in Python 2.7
    perimeters = []
    i=1
    while (i*i<N):
        if N%i == 0:
            perimeters.append(2*(i+(N//i)))
        i+=1
    if i*i == N:
        perimeters.append(2*(i+N//i))
    return min(perimeters)


def eqv(A):
    suml, sumr, mid= 0, sum(A), 0

    for i in range(len(A)):
        suml += mid
        sumr -= A[i]
        mid = A[i]

        if suml==sumr:
            return i

    return -1

# print(eqv([7,8,9,10,9,8,7]))
# print(eqv([]))
# print(eqv([3]))
# print(eqv([1,2,3,4,3,2]))




def pref_sums(A):
    n = len(A)
    P = [0]*(n+1)
    for k in xrange(1, n+1):
        P[k]=P[k-1]+A[k-1]
    return P

def sums(A):
    sum = 0
    P= [0]*(len(A)+1)
    for k in range(0,len(A)):
        sum +=A[k]
        # P.append(sum)
        P[k]=sum
    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

# print(pref_sums([1,2,3,4,5]))
# print(sums([1,2,3,4,5]))
# print(count_total([1,2,3,4,5,6,7], 2, 4))