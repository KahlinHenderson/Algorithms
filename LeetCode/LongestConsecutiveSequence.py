# Given an unsorted array of integers, nums, find and return the length of the
# longest sequence of consecutive integers. Let n be an integer in nums. If 
# n-1 is also in nums, then n is not the beginning of a sequence of consecutive
# integers. If n-1 is not in nums, then n is the beginning of a sequence of
# consecutive integers. The sequence may only contain n, or n and n+1, or n, n+1 and 
# n+2, etc.
def longestConsecutive(nums):
    numSet = Set(nums)
    longest = 0
    for n in nums:
        if n-1 not in numSet:
            length = 0
            while n + length in numSet:
                length += 1
            longest = max(length, longest)
    return longest
