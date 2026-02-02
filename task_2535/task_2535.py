# LeetCode #2535 | Difference Between Element Sum and Digit Sum of an Array | [EASY]

class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        array_sum = 0
        digit_sum = 0

        for n in nums:
            n_digit_sum = 0
            array_sum += n
            while(n != 0):
                n_digit_sum += (n % 10)
                n = n // 10
            digit_sum += n_digit_sum
        
        return abs(digit_sum-array_sum)