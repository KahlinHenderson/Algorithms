# Given a string s and a list of strings, dictionary, determine whether or not it's
# possible to use the list of strings to form s.
def wordBreak(s, dictionary):
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
    return dp[len(s)]
    
