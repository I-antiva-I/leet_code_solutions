# LeetCode #0217 | Contains Duplicate | [EASY]

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) == len(nums)