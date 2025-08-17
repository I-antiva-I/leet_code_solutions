# LeetCode #0075 | Sort Colors | [MEDIUM] 
# [!] IMPORTANT (Dutch National Flag Algorithm)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i_check = 0
        i_zero = 0
        i_two = len(nums)-1

        while i_check <= i_two:
            if nums[i_check] == 0:
                nums[i_check], nums[i_zero] = nums[i_zero], nums[i_check]
                i_check += 1
                i_zero += 1
            elif nums[i_check] == 1:
                i_check += 1
            else:
                nums[i_check], nums[i_two] = nums[i_two], nums[i_check]
                i_two -= 1
        