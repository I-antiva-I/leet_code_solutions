# LeetCode #0859 | Buddy Strings | [EASY]

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
        if len(s) != len(goal):
            return False

        if s == goal:
            chars = set()
            for char in s:
                if char in chars:
                    return True
                else:
                    chars.add(char)
            return False

        else:
            off_position = list()
            for i in range(len(s)):
                if s[i] != goal[i]:
                    off_position.append(i)
                    
            if len(off_position) == 2:
                off_1, off_2 = off_position
                return s[off_1] == goal[off_2] and s[off_2] == goal[off_1]
            else:
                return False