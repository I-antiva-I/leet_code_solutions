# LeetCode #3498 | Reverse Degree of a String | [EASY]

class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        degree = 0
        for i in range(len(s)):
            degree += (ord('z') - ord(s[i]) + 1)*(i+1)
        return degree