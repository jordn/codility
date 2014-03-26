import timeit
import time
import math

def fix(S):
    # write your code in Python 2.6
    print S
    max_length = 0

    for index in range(1, len(S)):
        prefix = S[:-index]
        suffix = S[index:]
        # print prefix, suffix
        if prefix == suffix:
            print prefix, suffix
            max_length = len(S) - index
            break

    return max_length


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
  S = "abbabba"
  print fix(S)
  S = "a"
  print fix(S)
  S = "abba8abba"
  print fix(S)
  S = "abbsadfsdafbba"
  print fix(S)
  S = "a"*1000000
  print fix(S)
  # S = 123321
  # print fix(S)


test()
