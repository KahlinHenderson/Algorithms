# Given a string s determine whether or not its alphanumeric characters form a
# palindrome. Note that we consider upper and lowercases to be the same.
def isPalindrome(s):
    res = ""
    for i in s:
        if i.isalnum():
            res += i.lower()
    n = len(res)
    l = 0
    r = n-1
    while l < r:
        if res[l] != res[r]:
            return False
        l += 1
        r -= 1
    return True
