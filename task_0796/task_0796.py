# LeetCode #0796 | Rotate String | [EASY]

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)

        if len(goal) != n:
            return False

        double_s = s+s

        for i in range(n):
            if double_s[i:n+i] == goal:
                return True
        
        return False