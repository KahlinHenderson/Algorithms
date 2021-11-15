# Given an m x n matrix return all elements of the matrix in spiral order.
def PrintSpiral(mat, top, bottom, left, right):
    if left > right:
        return
    for i in range(left, right + 1):
        print(mat[top][i], end = '')
    top = top + 1
    if top > bottom:
        return
    for i in range(top, bottom + 1):
        print(mat[i][right], end = '')
    right = right - 1
    if left > right:
        return
    for i in range(right, left - 1, -1):
        print(mat[bottom][i], end = '')
    bottom = bottom - 1
    if top > bottom:
        return
    for i in range(bottom, top - 1, -1):
        print(mat[i][left], end = '')
    left = left + 1
    PrintSpiral(mat, top, bottom, left, right)
