# LeetCode #0551 | Student Attendance Record I | [EASY]

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l_streak = 0
        a_total = 0

        for char in s:
            if char == "L":
                l_streak += 1
            else:
                l_streak = 0
                if char == "A":
                    a_total += 1
            
            if (l_streak == 3) or (a_total == 2):
                return False
        
        return True