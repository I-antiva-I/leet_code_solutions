# LeetCode #0500 | Keyboard Row | [EASY] |

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        only_one_row_words = []

        for word in words:
            current_row = 0
            for char in word:
                if (char.lower() in first_row):
                    if (current_row == 0):
                        current_row = 1
                    elif (current_row != 1):
                        current_row = 0
                        break

                if (char.lower() in second_row):
                    if (current_row == 0):
                        current_row = 2
                    elif (current_row != 2):
                        current_row = 0
                        break
                
                if (char.lower() in third_row):
                    if (current_row == 0):
                        current_row = 3
                    elif (current_row != 3):
                        current_row = 0
                        break

            if (current_row != 0):
                only_one_row_words.append(word)
       
        return only_one_row_words