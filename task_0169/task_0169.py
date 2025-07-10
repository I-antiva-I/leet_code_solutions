# LeetCode #0169 | Majority Element | [EASY]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        most_common = nums[0]
        mc_frequency = 1

        for num in nums[1:]:

            if num == most_common:
                mc_frequency += 1
            else:
                mc_frequency -= 1
                if mc_frequency == 0:
                    most_common = num
                    mc_frequency = 1
        
        return most_common
        