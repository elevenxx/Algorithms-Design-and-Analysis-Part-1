"""
input: array A of n distinct integers, left and right endpoints l, r
postcondition: elements of the subarray A[l], A[l+1],...,A[r]
are sorted from smallest to largest
output: keep track of the number of comparisons
high level explanation:
if l >= r: return
i = choosePivot(A, l, r)
swap A[i] and A[l] # make pivot first
j = partition(A, l, r) # the pivot's final position
quicksort(A, l, j-1)
quicksort(A, j+1, l)
mark: the reason why pivot choosing is important is that every pair
elements of array A has only 0 or 1 comparisons. If good pivot, most pairs
have not to compare at all, because the two elements are split in different
halves. If bad pivot, then most pairs have to compare once.
"""
import random
import sys


def quickSort(A, l, r, type):
    if l >= r:
        return 0
    i = choosePivot(A, l, r, type)
    A[i], A[l] = A[l], A[i]
    j = partition(A, l, r)
    C1 = quickSort(A, l, j - 1, type)
    C2 = quickSort(A, j + 1, r, type)
    return r - l + C1 + C2


def choosePivot(A, l, r, type):
    if type == 'first':
        return l
    elif type == 'last':
        return r
    elif type == 'random':
        return random.randint(l, r)
    elif type == 'median-of-three':
        mid = (l + r) // 2
        median = sorted([A[l], A[r], A[mid]])[1]
        return A.index(median)


# input: array A of n distinct integers, left and right endpoints l, r
# postcondition: elements of the subarray A[l], A[l+1],...,A[r]
# are partitioned around A[l]
# output: final position of pivot element
def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

if __name__ == '__main__':
    # [3, 8, 2, 5, 1, 4, 7, 6]
    # [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]
    A = []
    with open('problem5.6test2.txt', 'r') as f:
        for line in f:
            A.append(int(line.strip('\n').split(',')[0]))

    # 'first', 620; 'last', 573; 'random', undecided; 'median-of-three', 502
    type = 'median-of-three'
    if type == 'random':
        cnt = []; times = 10
        for _ in range(times):
            ans = quickSort(A, 0, len(A)-1, type)
            cnt.append(ans)
        count = sum(cnt) // times
    else:
        count = quickSort(A, 0, len(A) - 1, type)
    #print(A)
    print(count)