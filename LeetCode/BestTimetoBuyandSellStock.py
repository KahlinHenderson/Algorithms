# Let prices be an array that stores the price of a stock on the ith day. Find
# and return the maximum profit that can be made by buying on day i and selling 
# on a subsequent day.
def maxProfit(prices):
    l,r = 0, 1
    maxP = 0 
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP
