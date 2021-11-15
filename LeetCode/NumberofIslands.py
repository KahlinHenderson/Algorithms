# Given an m x n binary grid with each 0 representing water and each 1 
# representing land return the number of islands, where an island is a
# set of adjacent 1s that are connected horizontally or vertically.
def dfs(grid, r, c):
    grid[r][c] = 0
    lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for row, col in lst:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
            dfs(grid, row, col)

def numIslands(grid):
    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                dfs(grid, r, c)
            islands += 1
    return islands
    

