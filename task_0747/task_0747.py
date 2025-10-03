# LeetCode #0747 | Largest Number At Least Twice of Others | [EASY]

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first_largest_i = 0
        second_largest_i = 1

        if nums[first_largest_i] < nums[second_largest_i]:
            second_largest_i = 0
            first_largest_i = 1

        for i in range(2, len(nums)):
            if nums[i] > nums[first_largest_i]:
                second_largest_i = first_largest_i
                first_largest_i = i
            elif nums[i] > nums[second_largest_i]:
                second_largest_i = i
        
        if (nums[first_largest_i] >= nums[second_largest_i] * 2):
            return first_largest_i
        else:
            return -1
            