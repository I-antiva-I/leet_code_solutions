# LeetCode #1748 | Sum of Unique Elements | [EASY]

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_freq = {}
        unique_sum = 0

        for n in nums:
            num_freq[n] = num_freq.get(n, 0) + 1
        
        for n, freq in num_freq.items():
            if (freq == 1):
                unique_sum += n

        return unique_sum