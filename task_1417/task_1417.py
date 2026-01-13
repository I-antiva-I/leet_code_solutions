# LeetCode #1417 | Reformat The String | [EASY]

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        digits = []
        letters = []

        for char in s:
            if (char.isdigit()):
                digits.append(char)
            else:
                letters.append(char)
        
        if (abs(len(digits) - len(letters)) > 1):
            return ""
        
        result = []
        result.append(digits.pop()) if (len(digits) > len(letters)) else result.append(letters.pop())

        while ((len(digits) > 0) or (len(letters) > 0)):
            if (result[-1].isdigit()):
                result.append(letters.pop())
            else:
                result.append(digits.pop())
     
        return "".join(result)
