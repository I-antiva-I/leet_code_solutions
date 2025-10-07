# LeetCode #0806 | Number of Lines To Write String | [EASY]

class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        
        current_line_width = 0
        max_line_width = 100
        lines = 0

        for char in s:
            current_line_width += widths[ord(char)-97]
            if current_line_width > max_line_width:
                lines += 1
                current_line_width = widths[ord(char)-97]
        lines += 1

        return [lines, current_line_width]
