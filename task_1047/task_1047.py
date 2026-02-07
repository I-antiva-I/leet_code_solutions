# LeetCode #1047 | Remove All Adjacent Duplicates In String | [EASY]

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for char in s:
            if (stack):
                if (char == stack[-1]):
                    stack.pop()
                    continue
            stack.append(char)
        
        return "".join(stack)