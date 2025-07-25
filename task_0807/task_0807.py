# LeetCode #0807 | Max Increase to Keep City Skyline | [MEDIUM]

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        increase = 0

        row_maxs = []
        col_maxs = []

        for i in range(n):
            row_max = 0
            col_max = 0
            for j in range(n):
                if grid[i][j] > row_max:
                    row_max = grid[i][j] 
                if grid[j][i] > col_max:
                    col_max = grid[j][i]
            row_maxs.append(row_max)
            col_maxs.append(col_max)
        
        for i in range(n):
            for j in range(n):
                increase += min(row_maxs[i], col_maxs[j]) - grid[i][j]
    
        return increase