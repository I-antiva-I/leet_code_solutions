# LeetCode #0455 | Assign Cookies | [EASY]

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
    
        ns = len(s)
        if (ns == 0):
            return 0
        
        g.sort()
        s.sort()

        ng = len(g)
        index_greed = 0
        count = 0

        for cookie in s:
            if (index_greed == ng):
                break
            
            if (g[index_greed] <= cookie):
                index_greed += 1
                count += 1
            
        return count