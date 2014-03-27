def solution(A):
    # write your code in Python 2.6
    length = len(A)
    return (length+1)*(length+2)/2 - sum(A)