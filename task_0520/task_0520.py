# LeetCode #0520 | Detect Capital | [EASY]

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        return (word.upper() == word) or (word.lower() == word) or (word.capitalize() == word)