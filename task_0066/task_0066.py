# LeetCode #0066 | Plus One | [EASY]

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        ref = len(digits) - 1
        digits[ref] += 1

        while (ref > 0) and (digits[ref] > 9):
            digits[ref] = 0
            ref -= 1
            digits[ref] += 1
        
        if (ref == 0) and (digits[ref] > 9):
            digits[ref] = 0
            digits.insert(0, 1)

        return digits