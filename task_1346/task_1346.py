# LeetCode #1346 | Check If N and Its Double Exist | [EASY]

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        passed = set()
        
        for a in arr:
            if (((a*2) in passed) or ((a//2) in passed) and (a%2 == 0)):
                return True
            passed.add(a)
        
        return False