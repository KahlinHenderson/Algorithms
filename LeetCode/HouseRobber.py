# Suppose we are robbing a street that consists of n houses, but if we rob
# adjacent houses an alarm system is triggered. Given an array whose ith
# value is the amount stored in the ith house, find the maximum amount that
# can be robbed from the street.
def rob(ar):
    n = len(ar)
    if n == 0:
        return 0
    if n == 1:
        return ar[0]
    if n == 2:
        return max(ar[0], ar[1])
    dp = [0 for x in range(n)]
    dp[0] = ar[0]
    dp[1] = max(ar[0], ar[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + ar[i])
    return dp[n-1]
    
    
        

