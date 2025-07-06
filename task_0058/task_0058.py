 # LeetCode #0058 | Length of Last Word | [EASY]

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(s.strip("").split()[-1])