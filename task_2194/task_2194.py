# LeetCode #2194 | Cells in a Range on an Excel Sheet | [EASY]

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        int_from =  ord(s[1])
        int_to =    ord(s[4])
        char_from = ord(s[0])
        char_to =   ord(s[3])
        cells = []
                
        for c in range(char_from, char_to+1):
            for i in range(int_from, int_to+1):
                cells.append(chr(c)+chr(i))

        return cells