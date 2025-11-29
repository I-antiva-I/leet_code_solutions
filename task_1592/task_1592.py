# LeetCode #1592 | Rearrange Spaces Between Words | [EASY]

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """

        is_char_reached = False
        n_words = 0
        n_spaces = 0
        words = []

        for char in text:
            if is_char_reached:
                if char != " ":
                    words[n_words-1] += char
                else:
                    is_char_reached = False
                    n_spaces += 1
            else:
                if char != " ":
                    is_char_reached = True
                    words.append(char)
                    n_words += 1
                else:
                    n_spaces += 1
        
        if n_words == 1:
            return words[0] + " "*n_spaces

        spaces_between = n_spaces // (n_words-1)
        spaces_end = n_spaces % (n_words-1)

        result = words[0]
        for w in words[1:]:
            result += (" "*spaces_between) + w
        result += " "*spaces_end

        return result