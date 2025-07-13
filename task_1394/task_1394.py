# LeetCode #1394 | Find Lucky Integer in an Array | [EASY]

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        frequencies = {}
        for value in arr:
            if value in frequencies:
                frequencies[value] += 1
            else:
                frequencies[value] = 1 
        
        lucky = -1
        for k,v in frequencies.items():
            if (v == k) and (v > lucky):
                lucky = v
        
        return lucky