# We have a robot stationed at the top left corner of an m x n grid who, at any time,
# can only move down or to the right. Return the number of unique paths he can take
# to get to the bottom right corner.
def uniquepaths(m, n):
    myList = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            myList[i][j] = myList[i-1][j] + myList[i][j-1]
    return myList[-1][-1]
