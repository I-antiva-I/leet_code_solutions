# LeetCode #0171 | Excel Sheet Column Number | [EASY]

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        n = len(columnTitle) - 1
        number = 0

        for char in columnTitle:
            number += (((ord(char) - 65) % 26) + 1) * (26**n)
            n -= 1

        return number