# Given the root of a binary tree find and return its maximum depth. The maximum
# depth of a binary tree is the number of nodes in the longest path from the root
# node to the leaf node furthest from it.
def max_depth(root):
    if root == None:
        return 0
        
    left_depth = max_depth(root.left)
    
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)
    
