# LeetCode #0001 | Two Sum | [EASY]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        need = {}
        
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in need:
                return [i, need[delta]]
            need[nums[i]] = i
        
        return [-1]