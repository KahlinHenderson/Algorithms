# Given the root nodes p,q of two binary trees write a function that checks whether
# or not the binary trees are the same. Two binary trees are the same if they're
# structurally identical and their corresponding nodes have exactly the same values.
def isSameTree(p, q):
    if p is None and q is None:
        return True
    
    if p is None or q is None or p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
