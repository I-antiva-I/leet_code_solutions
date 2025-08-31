# LeetCode #0179 | Largest Number | [MEDIUM]

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    
        nums = sorted(map(str, nums), lambda a, b: cmp(b+a, a+b))
        return "0" if nums[0] == "0" else "".join(nums)
       