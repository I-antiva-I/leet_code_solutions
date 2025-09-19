# LeetCode #0070 | Climbing Stairs | [EASY]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def howManyFor(n, memo = [0]*45):
            if memo[n-1] != 0:
                return memo[n-1]
            if (n == 1):
                return 1
            if (n == 2):
                return 2
            memo[n-1] = howManyFor(n-1, memo) + howManyFor(n-2, memo)
            return memo[n-1]
        
        return howManyFor(n)