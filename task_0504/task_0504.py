# LeetCode #0504 | Base 7 | [EASY]

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if (num == 0):
            return "0"
        
        result = ""
        is_negative = bool(num < 0) 
        if is_negative:
            num = abs(num)
        
        while (num != 0):
            result = str(num % 7) + result
            num = num // 7
        
        return "-"+result if is_negative else result