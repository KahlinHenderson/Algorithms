# Suppose we have a staircase that takes n steps to get to the top and each time we
# climb we can go 1 or 2 steps. Return the number of unique ways we can get to the 
# top.
def climbStairs(n):
    if n == 1 or n == 2:
        return n
    prevprev = 1
    prev = 2
    current = 0
    for step in range(3, n+1):
        current = prevprev + prev
        prevprev = prev
        prev = current
    return current
