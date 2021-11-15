# Given the root node of a binary tree determine whether or not it is a valid
# binary search tree. A binary tree is a valid bst if for every node the value 
# in that node is greater than the value in any node of its left subtree and
# smaller than the value in any node of its right subtree.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
            
        if not(node.val > left and node.val < right):
            return False
            
        return (valid(node.left,left,node.val) and valid(node.right,node.val,right))
    
    return valid(root, float("-inf"), float("inf"))
    
