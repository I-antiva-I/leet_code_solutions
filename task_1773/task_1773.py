# LeetCode #1773 | Count Items Matching a Rule | [EASY]

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        count = 0
        rule_key_indexes = {
            "type" : 0,
            "color" : 1,
            "name" : 2
        }
        rule_index = rule_key_indexes[ruleKey]

        for item in items:
            count += 1 if (item[rule_index] == ruleValue) else 0

        return count