# LeetCode #2347 | Best Poker Hand | [EASY]

class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        
        count_suits = {}
        count_ranks = {}

        for s in suits:
            count_suits[s] = count_suits.get(s, 0) + 1
    
        for r in ranks:
            count_ranks[r] = count_ranks.get(r, 0) + 1

        max_cs = max(count_suits.values())
        max_cr = max(count_ranks.values())

        if (max_cs == 5):
            return "Flush"
        elif (max_cr >= 3):
            return "Three of a Kind"
        elif (max_cr == 2):
            return "Pair"
        else:
            return "High Card"
