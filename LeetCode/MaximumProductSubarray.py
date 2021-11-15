# Given an array of integers find and return the largest product of any subarray.
def findMaxProduct(A):
    max_ending = min_ending = 0
    max_so_far = 0
    for i in A:
        temp = max_ending
        
        max_ending = max(i, max(i * max_ending, i * min_ending))
        
        min_ending = min(i, min(i * temp, i * min_ending))
        
        max_so_far = max(max_so_far, max_ending)
    
    return max_so_far
