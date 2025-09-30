# LeetCode #0744 | Find Smallest Letter Greater Than Target| [EASY]

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        for char in letters:
            if (ord(char) > ord(target)):
                return char
        
        return letters[0]