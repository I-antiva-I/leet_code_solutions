# LeetCode #0674 | Longest Continuous Increasing Subsequence | [EASY]

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        streak = 1
        max_streak = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                streak += 1
                max_streak = max(streak, max_streak)
            else:
                streak = 1

        return max_streak