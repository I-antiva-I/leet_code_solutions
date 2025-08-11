# LeetCode #0485 | Max Consecutive Ones | [EASY]

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        streak = 0
        max_streak = 0
        
        for num in nums:
            if num == 1:
                streak += 1
            else:
                max_streak = max(streak, max_streak)
                streak = 0

        return max(streak, max_streak)