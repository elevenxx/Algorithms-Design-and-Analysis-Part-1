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
"""
import random


def quickSort(A, l, r, type):
    if l >= r:
        return 0
    i = choosePivot(A, l, r, type)
    A[i], A[l] = A[l], A[i]
    j = partition(A, l, r)
    C1 = quickSort(A, l, j - 1, type)
    C2 = quickSort(A, j + 1, r, type)
    return r-l+C1+C2


def choosePivot(A, l, r, type):
    if type == 'first':
        return l
    elif type == 'last':
        return r
    elif type == 'random':
        return random.randint(l, r)
    elif type == 'median-of-three':
        mid = (l + r) // 2
        three = [A[l], A[r], A[mid]]
        return sorted(three)[1]


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
    A = [3, 8, 2, 5, 1, 4, 7, 6, 10, 9, 0, 12, 14, 13, 20, 18, 19, 16, 15, 17, 11]
    type = 'median-of-three'
    ans = quickSort(A, 0, len(A)-1, type)
    print(A)
    print(ans)