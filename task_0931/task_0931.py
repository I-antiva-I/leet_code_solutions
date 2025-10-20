# LeetCode #0931 | Minimum Falling Path Sum | [MEDIUM] |

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
    
        n = len(matrix)
        total_cost = [cost for cost in matrix[0]]
    
        for r in range(1, n):
            row_cost = [cost for cost in total_cost]
            for c in range(n):
                # Single column
                if (c == 0) and (c == n-1):
                    row_cost[c] = matrix[r][c] + total_cost[c]
                # Left-most column
                elif (c == 0):
                    row_cost[c] = matrix[r][c] + min(total_cost[c], total_cost[c+1])
                # Right-most column
                elif (c == n-1):
                    row_cost[c] = matrix[r][c] + min(total_cost[c-1], total_cost[c])
                # Default column
                else:
                    row_cost[c] = matrix[r][c] + min(total_cost[c-1], total_cost[c], total_cost[c+1])
            total_cost = row_cost
        
        return min(total_cost)