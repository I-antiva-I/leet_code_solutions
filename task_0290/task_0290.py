# LeetCode #0290 | Word Pattern | [EASY]

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        words = s.split(" ")
        n = len(pattern)

        if (n != len(words)):
            return False   
        
        char_to_word = {}
        word_to_char = {}

        for i in range(n):
            char = pattern[i]
            word = hash(words[i])

            if (char in char_to_word):
                if word_to_char.get(word, None) != char:
                    return False
                    
            elif (word in word_to_char):
                return False

            else:
                char_to_word[char] = word
                word_to_char[word] = char

        return True