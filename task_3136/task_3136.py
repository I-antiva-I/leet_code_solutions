# LeetCode #3136 | Valid Word | [EASY]

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        is_alpha_num = word.isalnum()
        is_long_enough = len(word) >= 3
        has_vowel = False
        has_consonant = False

        for letter in word:
            if letter.isalpha():
                if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                    has_vowel = True
                else:
                    has_consonant = True
        
        return all([is_alpha_num, is_long_enough, has_vowel, has_consonant])
