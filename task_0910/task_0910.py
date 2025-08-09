# LeetCode #0910 | Smallest Range II | [MEDIUM]

class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        if n == 1:
            return 0 
        nums.sort()
        delta = nums[n-1] - nums[0]

        for i in range(n-1):
            upper = max(nums[i] + k, nums[n-1] - k)
            lower = min(nums[i+1] - k, nums[0] + k)
            if upper - lower < delta:
                delta = upper - lower

        return delta