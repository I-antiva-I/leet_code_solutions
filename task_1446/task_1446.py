# LeetCode #1446 | Consecutive Characters | [EASY]

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        streak = 0
        max_streak = 0
        streak_char = "?"

        for char in s:
            if char != streak_char:
                if streak > max_streak:
                    max_streak = streak
                streak_char = char 
                streak = 0       
            streak += 1

        max_streak = max(streak, max_streak)
        return max_streak