# LeetCode #3168 | Minimum Number of Chairs in a Waiting Room | [EASY]

class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        queue = 0
        max_size = 0
        
        for c in s:
            if (c == "E"):
                queue += 1
                max_size = max(max_size, queue)
            else:
                queue -=1
        
        return max_size