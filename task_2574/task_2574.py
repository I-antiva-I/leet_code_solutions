# LeetCode #2574 | Left and Right Sum Differences | [EASY]

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)

        right_sum = [0] * n
        left_sum = [0] * n
        deltas = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i-1] + nums[i-1]
            right_sum[n-1-i] = right_sum[n-i] + nums[n-i]

        for i in range(n):
            deltas[i] = abs(left_sum[i]-right_sum[i])

        return deltas