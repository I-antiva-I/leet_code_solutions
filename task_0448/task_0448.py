# LeetCode #0448 | Find All Numbers Disappeared in an Array | [EASY]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        freq = [0] * n
        missing = []

        for i in range(n):
            freq[nums[i]-1] += 1

        for i in range(n):
            if (freq[i] == 0):
                missing.append(i+1)
        
        return missing

        # (+) Alternative solution: no extra space and in O(n) runtime.
        """
        n = len(nums)
        missing = []

        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        for i in range(n):
            if (nums[i] > 0):
                missing.append(i+1)
        
        return(missing)
        """