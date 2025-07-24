# LeetCode #0028 | Find the Index of the First Occurrence in a String | [EASY]
# [!] IMPORTANT (KMP Algorithm)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        cursor = 0
        same_chars = 0
        n = len(haystack)
        f = len(needle)

        while ((cursor + same_chars < n) and (same_chars < f)):
            if haystack[cursor + same_chars] == needle[same_chars]:
                same_chars += 1
            else:
                cursor += 1
                same_chars = 0
                
        if same_chars == f:
            return cursor
        else:
            return -1 