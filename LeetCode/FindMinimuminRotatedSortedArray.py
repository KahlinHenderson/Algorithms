# Given a sorted array that's been rotated between 1 and n times find the minimum
# value of the rotated array. Note that after rotating the array
# A[0],...,A[n-1] 1 time we get A[n-1],A[0],A[1],...,A[n-2].
def findmin(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = start + ((end - start) // 2)
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid + 1
    return nums[start]
    
