"""
input: An array A of n numbers, in arbitrary order,
and an integer ith, ith is in [1, n]
output: the ith-smallest element of A
choose a random pivot
partition the input array around the pivot
recurse appropriately
"""

import random


def rselect(A, l, r, ith):
    if l >= r:
        return A[l]
    rp = random.randint(l, r)
    A[rp], A[l] = A[l], A[rp]
    j = partition(A, l, r)
    if j == ith:
        return A[j]
    elif j > ith:
        return rselect(A, l, j - 1, ith)
    else:
        return rselect(A, j + 1, r, ith)

# return final position of pivot in array
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
    # A = [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]
    A = []
    with open('problem5.6test2.txt', 'r') as f:
        for line in f:
            A.append(int(line.strip('\n').split(',')[0]))

    # in python, 50th order statistic is in 50-1=49 final position
    ans = rselect(A, 0, len(A)-1, 50-1)
    # print(A)
    print(ans)