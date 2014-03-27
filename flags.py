
def findpeaks(A):
    peaks = [0]
    if len(A)>2:
        for index in range(1, len(A)-1):
            if A[index-1] < A[index] > A[index+1]:
                peaks.append(1)
            else:
                peaks.append(0)
            # print index, value
        return peaks

    else: 
        return [0]

# def distancetopeaks(A):
#     distance = []
#     for element in A:
#         if element == 1

def flags(A):
    print A
    peaks = findpeaks(A)
    print peaks
    # max flags upper limit is no of peaks
    num_flags = sum(peaks)
    index = 0
    flags_remaining = num_flags
    while flags_remaining > 0:
        print "Trying", num_flags, "flags"
        while index < len(peaks):
            # print index
            if peaks[index] == 1:
                # jump by number of flags
                # print "Flag at ", index
                flags_remaining -= 1
                index += num_flags
            else:
                index +=1
        if flags_remaining <= 0:
            # print "all flags planted"
            break
        else:
            # print "flags remain :("
            index = 0
            num_flags -= 1
            flags_remaining = num_flags

    # print "Flags remaining:", flags_remaining
    print "Flags planted:", num_flags

    return num_flags


A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
print flags(A)


A = [1, -5, 3, 4, -3, 4, 1, 2, 3, 4, 6, 2]
print flags(A)

A = [1]
print flags(A)

A = [1,2]
print flags(A)

A = [1,2,1]*23
print flags(A)

A = [2334532,32543425,23453245,-3245342345,3245,23]
print flags(A)