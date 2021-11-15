# Given a string return the longest palindromic substring.
def expand(str, low, high):
    length = len(str)
    while low >= 0 and high < length and str[low] == str[high]:
        low = low-1
        high = high+1
    return str[low+1:high]
def findLongestPalindromicSubstring(str, length):
    max_str = ""
    max_length = 0
    n = length
    for i in range(n):
        
        curr_str = expand(str, i, i)
        curr_length = len(curr_str)
        
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
        
        curr_str = expand(str, i, i+1)
        curr_length = len(curr_str)
       
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str
    
    return max_str
        
