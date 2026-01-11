# LeetCode #0274 | H-Index | [MEDIUM]

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        h = 0
        citations.sort(reverse=True)

        for i in range(len(citations)):
            h = max(min(i+1, citations[i]), h)

        return  h