import math

def solution(X, Y, D):
    # write your code in Python 2.6
    return int(math.ceil((Y-X)/float(D)))



print solution(10, 85, 30)
assert solution(10, 85, 30) is 3