# LeetCode #2544 | Alternating Digit Sum | [EASY]

import math

class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        alt_d_sum = 0
        stack = []
        sign = 1

        while (n != 0):
            stack.append((n % 10))
            n = n // 10
        
        for i in range(len(stack)-1, -1, -1):
            alt_d_sum += stack[i]*sign
            sign = sign*-1

        return alt_d_sum