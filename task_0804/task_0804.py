# LeetCode #0804 | Unique Morse Code Words| [EASY]

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # One liner solution
        # return len({''.join(morse[ord(c)-97] for c in w) for w in words})

        codes = set()

        for word in words:
            code = ""
            for char in word:
                code += morse[ord(char)-97]
            codes.add(code)
        
        return len(codes)