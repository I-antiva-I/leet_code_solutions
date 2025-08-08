# LeetCode #0908 | Smallest Range I | [EASY]

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        max_value = nums[0]
        min_value = nums[0]

        for n in nums:
            if n > max_value:
                max_value = n
            if n < min_value:
                min_value = n
        
        if (max_value - k ) > (min_value + k):
            return (max_value - min_value - 2*k) 
        else:
            return 0