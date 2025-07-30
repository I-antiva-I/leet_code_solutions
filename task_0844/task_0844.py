# LeetCode #0844 | Backspace String Compare | [EASY]

class Solution(object):

    def backspaceRemove(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for char in s:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return self.backspaceRemove(s) == self.backspaceRemove(t)