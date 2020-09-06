"""
an unimodal array: increasing order until its maximum, after which in decreasing order
input: an array A, and its lower and upper bound
output: maximum element in A
algorithm: divide and conquer
"""

def maxUnimodal(A, low, high):
    if low == high:
        return A[low]
    elif low == high - 1:
        return max(A[low], A[high])
    mid = (low + high) // 2
    if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
        return A[mid]
    elif A[mid-1] < A[mid] < A[mid+1]:
        return maxUnimodal(A, mid+1, high)
    else:
        return maxUnimodal(A, low, mid-1)


if __name__ == '__main__':
    mylist = [1, 3, 50, 10, 9, 7, 6]
    ans = maxUnimodal(mylist, 0, len(mylist)-1)
    print(ans)