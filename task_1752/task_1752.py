# LeetCode #1752 | Check if Array Is Sorted and Rotated | [EASY]

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_n = max(nums)
        min_n = min(nums)
        has_meet_original_end = False
        n = len(nums)

        for i in range(n):
            if (nums[(i-1+n) % n]) <= (nums[(i+n) % n]):
                continue
            else:
                if ((nums[(i-1+n) % n] == max_n) and (nums[(i+n) % n] == min_n) and (not has_meet_original_end)):
                    has_meet_original_end = True
                else:
                    return False
        
        return True