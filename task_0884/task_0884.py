# LeetCode #0884 | Uncommon Words from Two Sentences | [EASY]

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
        words = {}
        unique = []

        for w in s1.split():
            if w in words:
                words[w] += 1
            else:
                words[w] = 1

        for w in s2.split():
            if w in words:
                words[w] += 1
            else:
                words[w] = 1
        
        for k,v in words.items():
            if v == 1:
                unique.append(k)
        
        return unique