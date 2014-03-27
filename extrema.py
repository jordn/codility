import time
import math


def findpeaks(A):
    print A
    peaks = []
    for index, value in enumerate(A):
        if A[index-1] < value > A[index+1]:
            peaks.append(1)
        else:
            peaks.append(0)
        # print index, value
    return peaks

# Can find extrema by running through keeping track of just the last three different values
# middle value is > than others --> maxima etc.
# edges are messy, but as we only need the total number of extrema
# and they're always going to be an extrema
# there will always be one, if there's an extrema in between the end will be a different extrema

def extrema(A):
    # write your code in Python 2.6
    # print A
    prev_val = None
    midd_val = None
    next_val = None
    num_extrema = 0


    for index in range(0 , len(A)):

        if A[index] != next_val:
            prev_val = midd_val

            if midd_val is None and next_val is not None:
                num_extrema += 1
            midd_val = next_val

            if next_val is None:
                num_extrema += 1
            next_val = A[index]


            if prev_val is not None and midd_val is not None and next_val is not None:
                if prev_val < midd_val > next_val:
                    # maxima
                    # print "maxima"
                    num_extrema += 1

                if prev_val > midd_val < next_val:
                    # minima
                    # print "minima"
                    num_extrema += 1
        # print "> ", A[index],"    " ,prev_val, midd_val, next_val, '(', num_extrema,')'

        # else:
            # continue

    return num_extrema


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
  A = [2,2,3,4,3,3,2,2,1,1,2,5]
  number = extrema(A)
  print "NUM EXTREMA: ", number

  A = [2,2]
  number = extrema(A)
  print "[2,2]: ", number

  A = [2,3]
  number = extrema(A)
  print "[2,3]: ", number

  A = [2,3,2]
  number = extrema(A)
  print "[2,3,2]: ", number


  A = [2]
  number = extrema(A)
  print "[2]: ", number


  A = [2,4,2]
  number = extrema(A)
  print "[2, 4, 2]: ", number










  A = [-2,-2,-3,-4,-3,-3,-2,-2,-1,-1,-2,-5]
  number = extrema(A)
  print "NUM EXTREMA: ", number

  A = [-2,-2]
  number = extrema(A)
  print "[-2,-2]: ", number

  A = [-2,-3]
  number = extrema(A)
  print "[-2,-3]: ", number

  A = [2,3,2]
  number = extrema(A)
  print "[2,3,2]: ", number


  A = [-2]
  number = extrema(A)
  print "[-2]: ", number


  A = [-2,-4,-2]
  number = extrema(A)
  print "[-2, -4, -2]: ", number

  A = [1,0]*100000
  number = extrema(A)
  print "[1,0]*100000: ", number

test()
