# LeetCode #0031 | Next Permutation | [MEDIUM]

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        ref_a = (n-2) % n
        ref_b = (n-1) 

        # Find first number (A) that is lower than previous.
        while (ref_a != n-1) and (nums[ref_a] >= nums[ref_a+1]):
            ref_a = n-1 if (ref_a == 0) else ref_a-1

        # Find first number that is greater than found number (A).
        while (ref_b != ref_a) and (nums[ref_a] >= nums[ref_b]):
          ref_b = ref_b-1

        # Swap (A) and (B).
        nums[ref_a], nums[ref_b] = nums[ref_b], nums[ref_a]

        # Swap other numbers after (A).
        ref_a = (ref_a + 1) % n
        ref_b = n-1
        while (ref_a < ref_b):
                nums[ref_a], nums[ref_b] = nums[ref_b], nums[ref_a]
                ref_a += 1
                ref_b -= 1

