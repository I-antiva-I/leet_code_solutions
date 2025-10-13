# LeetCode #0916 | Word Subsets | [MEDIUM] |

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        requred_chars = {}
        checked_chars = {}

        for word in words2:
            checked_chars = {}
            for char in word:
                checked_chars[char] = checked_chars.get(char, 0) + 1
                requred_chars[char] = max(requred_chars.get(char, 0), checked_chars[char])
        
        universal_words = []

        for word in words1:
            checked_chars = {}
            for char in word:
                checked_chars[char] = checked_chars.get(char, 0) + 1
                    
            is_universal = True
            for char, freq in requred_chars.items():
                if (freq > checked_chars.get(char, 0)):
                    is_universal = False
                    break
                    
            if is_universal:
                universal_words.append(word)
        
        return universal_words