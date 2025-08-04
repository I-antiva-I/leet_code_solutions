# LeetCode #0868 | Binary Gap | [EASY]

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        streak = 0
        max_streak = 0
        has_seen_one = False

        while n != 0:
            r = n % 2
            n = n // 2

            if r == 1:
                if streak > max_streak:
                    max_streak = streak
                streak = 1
                has_seen_one = True
            elif has_seen_one:
                streak += 1

        return max_streak