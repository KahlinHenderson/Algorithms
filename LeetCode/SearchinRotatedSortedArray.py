# Let nums be a sorted array of distinct integers. Let k be a pivot index that rotates
# the array into [nums[k], nums[k+1],...,nums[n-1], nums[o], nums[1],..., nums[k-1]]
# Given this rotated array, nums, and an integer, target, return the index of target if
# it exists in nums. If not, return -1.
def search(nums, target):
    l,r = 0, len(nums) -1
    while l <= r:
        mid = l + r // 2
        if target == nums[mid]:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1
