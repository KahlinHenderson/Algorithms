# Let a1,...,an be nonnegative integers such that ai is the point at coordinate
# (i, ai). Draw n vertical lines such that the ith line has its endpoints at 
# coordinates (i, ai) and (i, 0). Find the two lines that, along with the x-axis,
# give us a container that holds the most water.
def maxArea(A):
    l = 0
    r = len(A) - 1
    area = 0
    while l < r:
        area = max(area, min(A[l], A[r]) * r-l)
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area
