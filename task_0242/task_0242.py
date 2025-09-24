# LeetCode #0242 | Valid Anagram | [EASY]

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        letters_s = {}
        letters_t = {}

        for char in s:
            letters_s[char] = letters_s.get(char, 0) + 1
        
        for char in t:
            letters_t[char] = letters_t.get(char, 0) + 1
            
        if len(letters_t) == len(letters_s):
            for k in letters_s.keys():
                if letters_s.get(k, -1) != letters_t.get(k, -1):
                    return False
            return True
        else:
            return False