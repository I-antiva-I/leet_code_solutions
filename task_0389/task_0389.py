# LeetCode #0389 | Find the Difference | [EASY]

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        diff = 0
        for i in range(len(s)):
            diff += ord(t[i])-ord(s[i])
        
        return chr(diff+ord(t[-1]))