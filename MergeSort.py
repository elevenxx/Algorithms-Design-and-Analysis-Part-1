"""
input: array of n integers
output: array of same integers, sorted from smallest to largest
"""
def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        C, D = A[:mid], A[mid:]
        mergeSort(C)
        mergeSort(D)
        i, j = 0, 0
        k = 0
        while i < len(C) and j < len(D):
            if C[i] < D[j]:
                A[k] = C[i]
                i += 1
            else:
                A[k] = D[j]
                j += 1
            k += 1
        if i < len(C):
            A[k:] = C[i:]
        if j < len(D):
            A[k:] = D[j:]



if __name__ == "__main__":
    myList = [54, 26, 93, 0, 17, 77, 31, 44, 55, 20, 0]
    mergeSort(myList)
    print(myList)
