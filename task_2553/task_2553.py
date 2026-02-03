# LeetCode #2553 | Separate the Digits in an Array | [EASY]

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        digits = []

        for n in nums:
            temp = []
            while(n!=0):
                temp.append(n % 10)
                n = n // 10
            digits.extend(temp[::-1])
        
        return digits