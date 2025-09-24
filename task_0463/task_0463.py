# LeetCode #0463 | Island Perimeter | [EASY] 

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        p = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:

                    p += 4

                    if (i > 0) and (grid[i-1][j] == 1):
                        p -= 2
                    if (j > 0) and (grid[i][j-1] == 1):
                        p -= 2

        return p