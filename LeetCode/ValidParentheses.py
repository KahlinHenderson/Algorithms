# Given a string s that only contains the characters '(', ')', '{', '}', '[' and ']'
# determine whether or not the string is valid. The string s is invalid if,
# 1. s contains a closing bracket that's not preceeded by any opening brackets, or
# 2. s contains an opening bracket that's directly followed by a closing bracket of a 
#    different type.
def isValid(s):
    def is_matched_parentheses(left, right):
        return left == '(' and right == ')' or left == '{' and right == '}'
            or left == '[' and right == ']'
    stack = []
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if not stack or not is_matched_parentheses(stack[-1], ch):
                return False
            else:
                stack.pop()
    return not stack
