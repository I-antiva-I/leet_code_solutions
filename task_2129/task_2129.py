# LeetCode #2129 | Capitalize the Title | [EASY]

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        stack = []

        for word in title.split():
            stack.append(word.capitalize() if len(word) > 2 else word.lower())

        return " ".join(stack)