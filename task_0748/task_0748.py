# LeetCode #0748 | Shortest Completing Word | [EASY]

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        def breakdownLetters(word):
            breakdown = dict()
            for char in word:
                if (char.isalpha()):
                    breakdown[char.lower()] = breakdown.get(char.lower(), 0) + 1
            return breakdown

        required_letters = breakdownLetters(licensePlate)

        min_word_length = 1001
        min_word_index = -1
        
        for i in range(len(words)):
            all_letters = breakdownLetters(words[i])
            has_required = True
        
            for letter, occurences in required_letters.items():
                lookup = all_letters.get(letter, -1)
        
                if (lookup < occurences):
                    has_required = False
                    break

            if ((has_required) and (len(words[i]) < min_word_length)):
                min_word_length = len(words[i])
                min_word_index = i
        
        return words[min_word_index]
            