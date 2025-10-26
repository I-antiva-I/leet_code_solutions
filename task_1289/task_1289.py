# LeetCode #1289 | Minimum Falling Path Sum II | [HARD] |
# [!] CAN BE IMPROVED 

class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        total_cost = [cost for cost in grid[0]]
    
        for r in range(1, n):
            row_cost = [cost for cost in total_cost]
            for c in range(n):
                row_cost[c] = grid[r][c] + min(total_cost[:c] + total_cost[c+1:])
            total_cost = row_cost
        
        return min(total_cost)