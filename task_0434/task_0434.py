# LeetCode #0434 | Number of Segments in a String | [EASY]

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        is_char_reached = False
        n_words = 0

        for char in s:
            if is_char_reached:
                if char == " ":
                    is_char_reached = False
            else:
                if char != " ":
                    is_char_reached = True
                    n_words += 1
        
        return n_words