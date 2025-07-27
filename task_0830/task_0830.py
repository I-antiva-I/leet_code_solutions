# LeetCode #0830 | Positions of Large Groups | [EASY]

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        
        char = "?"
        streak = 0 
        groups = []

        for i in range(len(s)):
            if s[i] == char:
                streak += 1
            else:
                if consecutive > 2:
                    groups.append([i-streak, i-1])
                streak = 1
                char = s[i]

        if streak > 2:
            groups.append([len(s)-streak, len(s)-1])

        return groups