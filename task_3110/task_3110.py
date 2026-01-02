# LeetCode #3110 | Score of a String | [EASY]

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prev_char = s[0]
        score = 0

        for char in s[1:]:
            score += abs(ord(prev_char)-ord(char))
            prev_char = char

        return score