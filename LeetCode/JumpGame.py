# Let nums be an array of nonnegative integers, where each integer represents the 
# maximum jump length from that position. Starting from the oth index determine
# whether or not it's possible to reach the last index.
def canJump(nums):
    if len(nums) == 1:
        return True
    minstepsrequired = 0
    previousGood = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        minstepsrequired = previousGood - i
        if nums[i] >= minstepsrequired:
            previousGood = i
    return previousGood == 0
