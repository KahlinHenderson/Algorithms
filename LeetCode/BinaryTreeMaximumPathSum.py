# A path in a binary tree is a sequence of nodes such that for any pair of adjacent
# nodes there's an edge connecting them. Given the root of a binary tree find the
# maximum path sum in the tree.
def maxSum(root):
    if root is None:
        return 0
    left = max(0, maxSum(root.left))
    right = max(0, maxSum(root.right))
    currentSum = left + right + root.val
    maxSum = max(currentSum, maxSum)
    return max(left + node.val, right + node.val)
