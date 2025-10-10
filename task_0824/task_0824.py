# LeetCode #0824 | Goat Latin | [EASY] | 

class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        
        words = sentence.split(" ")

        for i in range(len(words)):
            if words[i][0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                words[i] += "ma"
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"
            
            words[i] += "a"*(i+1)

        return " ".join(words)