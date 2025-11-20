# LeetCode #2525 | Categorize Box According to Criteria | [EASY]

class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        
        is_heavy = (mass >= 100)
        is_bulky = ((length >= 10000) or 
                    (width >= 10000) or  
                    (height >= 10000) or 
                    (length*width*height >= 1000000000))

        
        if (is_heavy and is_bulky):
            return "Both"
        elif (is_heavy):
            return "Heavy"
        elif (is_bulky):
            return "Bulky"
        else:
            return "Neither"