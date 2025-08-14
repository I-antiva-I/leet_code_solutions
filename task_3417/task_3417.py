# LeetCode #3417 | Zigzag Grid Traversal With Skip | [EASY]

class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        m = len(grid[0])
        visited = []

        for i in range(n):
            temp = []
            for j in range(m):
                if (i+j) % 2 == 0:
                    if i % 2 == 0:
                        temp.append(grid[i][j])
                    else:
                        temp.insert(0, grid[i][j])
            visited += temp

        return visited