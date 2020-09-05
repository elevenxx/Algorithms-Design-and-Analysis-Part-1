"""
input: array A of n distinct integers
output: sorted array B with the same integers, and the number of inversions of A
inversion: an inversion of an array is a pair of elements that are out of order
divide and conquer
1.leftInv: an inversion with i, j both in the first half of A
2.rightInv: an inversion with i, j both in the second half of A
3.splitInv: an inversion with i in the first half, j in the second half
not use another place to store array B, sort only in place, so return array is also A
"""


def sortCountInv(A):
    # base case
    if len(A) <= 1:
        return (A, 0)
    else:
        mid = len(A) // 2
        # divide
        C, D = A[:mid], A[mid:]
        # conquer
        (C, leftInv) = sortCountInv(C)
        (D, rightInv) = sortCountInv(D)
        # combine
        # merge and count split Inversions
        splitInv = 0
        i, j = 0, 0
        k = 0
        while i < len(C) and j < len(D):
            if C[i] < D[j]:
                A[k] = C[i]
                i += 1
            else:
                A[k] = D[j]
                j += 1
                splitInv += len(C) - i
            k += 1
        if i < len(C):
            A[k:] = C[i:]
        if j < len(D):
            A[k:] = D[j:]

        return (A, leftInv + rightInv + splitInv)


if __name__ == "__main__":
    myList = [9, 8, 7, 6, 5, 4, 3, 2, 1] # 36
    myList2 = [54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777, 49689, 9083] # 28
    ans = sortCountInv(myList)
    print(ans)
