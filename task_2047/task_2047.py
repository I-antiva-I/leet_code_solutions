# LeetCode #2047 | Number of Valid Words in a Sentence | [EASY] |

class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def isValid(word):
            has_hyphen = False
            n = len(word)

            for i in range(n):
                # Case
                if ((word[i].isalpha()) and not(word[i] == word[i].lower())):
                    return False
                # Hyphen
                elif (word[i] == "-"):
                    if (i == 0) or (i == n-1) or (has_hyphen):
                        return False
                    has_hyphen = True
                    if (not(word[i-1].isalpha()) or not(word[i+1].isalpha())):
                        return False
                # Punctuation
                elif ( ((word[i] == "!") or (word[i] == ".") or (word[i] == ",")) and (i != n-1)):
                    return False
                # Digit
                elif (word[i].isdigit()):
                    return False
            # OK
            return True
                
        valid_words = 0

        for w in sentence.split():
            valid_words += 1 if isValid(w) else 0
            
        return valid_words
