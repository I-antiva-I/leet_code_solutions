# LeetCode #0724 | Find Pivot Index | [EASY]

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        index_sums = [0] * len(nums)
        other_half = 0

        index_sums[0] = total - nums[0]
        if index_sums[0] == other_half:
            return 0

        for i in range(1, len(index_sums)):
            other_half += nums[i-1]
            index_sums[i] = index_sums[i-1] - nums[i] 
            if index_sums[i] == other_half:
                return i
        
        return -1
