# Given the root of a binary tree perform a level order traversal and return each
# value of each node on every level.
def levelorder(root):
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
    return res
