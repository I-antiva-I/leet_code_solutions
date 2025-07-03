# LeetCode #0020 | Valid Parentheses | [EASY]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        expectation = []
        for char in s:
            if char == "{":
                expectation.append("}")
            elif char == "[":
                expectation.append("]")
            elif char == "(":
                expectation.append(")")
            elif len(expectation) == 0 or char != expectation.pop():
                return False

        return False if len(expectation) != 0 else True