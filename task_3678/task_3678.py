# LeetCode #3678 | Smallest Absent Positive Greater Than Average | [EASY]

class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        s = sum(nums)
        target = max((s // n) + 1, 1)
      
        while (True):
            if (target not in nums):
                return target
            else:
                target += 1
                