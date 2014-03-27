import time
import math


def prefixsum(A):
    N = len(A)
    p = [0] * (N+1)
    for k in xrange(1, N+1):
        p[k] = p[k-1] + A[k-1]
    return p

def suffixsum(A):
    N = len(A)
    p = [0] * (N + 1)
    for k in xrange(1, N+1):
        # print k
        p[-k-1] = p[-k] + A[-k]
    return p


def equi(A):
    # write your code in Python 2.6
    print A
    N = len(A)
    left = 0
    right = sum(A)
    for i in xrange(0, N):
        right = right - A[i]
        print left, right, '(',i,')'
        if left == right:
            print i
            return i
        left = left + A[i]
    print "None"
    return -1


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap    


@timing
def test():
  A = [-7, 1, 5, 2, -4, 3, 0]
  equi(A)
  A = [0]
  equi(A)
  A = [1,2,3,3,2,1]
  equi(A)
  A = [1,0,1]
  equi(A)
  A = [-2147483649]
  equi(A)
  A = [-1342285824, -1342303230, -1342285824]
  equi(A)
  A = [2, -1, -2, 1, 500]
  equi(A)

  A = [-1]*10000
  equi(A)

test()