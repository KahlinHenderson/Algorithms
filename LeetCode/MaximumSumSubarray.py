# Given an integer array A find and return the largest sum of any subarray.
def KadaneNeg(A):
    max_so_far = A[0]
    max_ending_here = A[0]
    for i in range(1, len(A)):
        max_ending_here = max_ending_here + A[i]
        
        max_ending_here = max(max_ending_here, A[i])
        
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far
