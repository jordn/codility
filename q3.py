import math

def solution(A):
    print A
    sortedA = sorted(A)
    print sortedA
    distance = []
    for index in range(1, len(sortedA)):
        distance.append(sortedA[index] - sortedA[index-1])

    print distance
    return min(distance)


A = [8,24,3,20,1,17]
print solution(A)

A = [7,21,3,42,3,7]
print solution(A)


A = [4,9]
print solution(A)

A = [23325254,32222339]
print solution(A)


A = [23,32222339]*2312
print solution(A)
