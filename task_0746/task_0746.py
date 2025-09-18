# LeetCode #0746 | Min Cost Climbing Stairs | [EASY]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        total_cost = [0]*(n+1)
        
        for i in range(2, n+1):
            total_cost[i] = min(total_cost[i-1]+cost[i-1], total_cost[i-2]+cost[i-2])
        
        return total_cost[n]