# LeetCode #0917 | Reverse Only Letters | [EASY]

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        left = 0
        right = len(s)-1
        all_chars = list(s)
        
        while(left < right):
            if not all_chars[left].isalpha():
                left += 1
                continue
            if not all_chars[right].isalpha():
                right -= 1
                continue
            
            all_chars[left], all_chars[right] = all_chars[right], all_chars[left]
            left += 1
            right -= 1

        return "".join(all_chars)