# LeetCode #0896 | Monotonic Array | [EASY]

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        changing = 0

        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] > 0:
                if changing == -1:
                    return False
                changing = 1
            elif nums[i]-nums[i-1] < 0:
                if changing == 1:
                    return False
                changing = -1
        
        return True