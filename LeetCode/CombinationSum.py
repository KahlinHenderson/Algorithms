# Given an array of distinct integers, candidates, and an integer, target, return
# a list of all combinations of integers that have a sum equal to target.
def combinationsum(candidates, target):
    ans = []
    tmp = []
    def helper(idx, total):
        if total > target:
            return
        if total == target:
            ans.append(tmp[:])
            return
        for i in range(idx, len(candidates)):
            total += candidates[i]
            tmp.append(candidates[i])
            helper(i, total)
            tmp.pop()
            total -= candidates[i]
    total = 0
    helper(0, total)
    return ans
