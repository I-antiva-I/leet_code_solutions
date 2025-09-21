# LeetCode #0202 | Happy Number | [EASY]

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        usual_suspects = set()

        while (n not in usual_suspects):
            usual_suspects.add(n)
            s = 0
            while (n != 0):
                s += (n % 10)**2
                n //= 10
            if s == 1:
                return True
            n = s
        return False