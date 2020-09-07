"""
input: n-by-n grid M of distinct numbers, and its dimension n
output: a local minimum in grid, which is smaller than above, below, left and right
1. brute force, O(n^2)

2. hint from 1-D minimum: look at center column, find minimum in this column,
if local minimum, return it; else, smaller left/right neighbor, minimum in that column,
recurse in left/right half. Base case: only 1 column, return max within.
O(n) time to find minimum in column, O(logn) iterations, like binary search,
O(nlogn) time total

3. O(n) time solution: divide n-by-n grid into four n/2-by-n/2 grid, like quadrant
look at boundary, center row and center column
find min within, if it's a local minimum, return it;
else: find smaller neighbor, recurse in that quadrant

reference:
http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
https://ideone.com/K3ggGm
"""

def findLocalMinLinearTime(M, n):
    return helperColumn(M, n, 0, n-1, 0, n-1)

# helper function that split on the middle column
def helperColumn(M, n, loCol, hiCol, loRow, hiRow):
    if loCol == hiCol:
        return min(M[loRow:hiRow+1][loCol])
    midCol = (loCol+hiCol) // 2
    tmp = min(M[loRow:hiRow+1][midCol])
    central, left, right = True, False, False
    if midCol-1 >= 0:
        for row in range(loRow, hiRow+1):
            if M[row][midCol-1] < tmp:
                tmp = M[row][midCol-1]
                central = False
                left = True
    if midCol+1 < n:
        for row in range(loRow, hiRow+1):
            if M[row][midCol+1] < tmp:
                tmp = M[row][midCol+1]
                central = False
                left = False
                right = True
    if central: return tmp
    if right: return helperRow(M, n, midCol+1, hiCol, loRow, hiRow)
    if left: return helperRow(M, n, loCol, midCol-1, loRow, hiRow)

# helper function that split on the middle row
def helperRow(M, n, loCol, hiCol, loRow, hiRow):
    if loRow == hiRow:
        return min(M[loRow][loCol:hiCol+1])
    midRow = (loRow+hiRow) // 2
    tmp = min(M[midRow][loCol:hiCol+1])
    central, up, down = True, False, False
    if midRow-1 >= 0:
        for col in range(loCol, hiCol+1):
            if M[midRow-1][col] < tmp:
                tmp = M[midRow-1][col]
                central = False
                up = True
    if midRow+1 < n:
        for col in range(loCol, hiCol+1):
            if M[midRow+1][col] < tmp:
                tmp = M[midRow+1][col]
                central = False
                up = False
                down = True
    if central: return tmp
    if up: return helperColumn(M, n, loCol, hiCol, loRow, midRow-1)
    if down: return helperColumn(M, n, loCol, hiCol, midRow+1, hiRow)

if __name__ == "__main__":
    Matrix = [[1, 3, 2, 5, 7], [0, 9, 10, 20, -3], [-8, 8, 4, 99, 100], [55, 21, -67, 88, -77],[13, -23, 99, 15, 33]]
    n = len(Matrix)
    ans = findLocalMinLinearTime(Matrix, n)
    print(ans)