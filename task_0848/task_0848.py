# LeetCode #0848 | Shifting Letters | [MEDIUM]

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

        total_shift = sum(shifts)
        result = ""

        for i in range(len(s)):
            result += chr( (ord(s[i]) - 97 + total_shift) % 26 + 97 )
            total_shift -= shifts[i]

        return result