import math

def chunkify(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

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

def maxblocks(A):
    # write your code in Python 2.6
    peaks = findpeaks(A)
    print peaks
    number_chunks = 1
    max_chunks = 1
    while number_chunks < len(peaks):

        empty = False
        chunksize = len(peaks)/number_chunks
        chunks = list(chunkify(peaks, chunksize))
        # print chunks

        for chunk in chunks:
            if sum(chunk) < 1:
                empty = True
                break
        # print empty
        if empty:
           break
        else:
            max_chunks = number_chunks
        number_chunks += 1
            

    return max_chunks


A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
A = [5]
print maxblocks(A) #3
A = [1,2,3,4,5,6]  #no peaks
print maxblocks(A) #3
A = [0,1,0,1,0,1,0,1,0,1,0] #prime length
print maxblocks(A) #3
A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
A = [1,2,3,4,3,4,1,2,3,4,6,2]
print maxblocks(A) #3
B = [1,2,1,2,1,1,1,1,1,2,1,1]
print maxblocks(B) #3

# assert maxpeaks(A) is 3