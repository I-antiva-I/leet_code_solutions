# LeetCode #3527 | Find the Most Common Response | [MEDIUM]

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """

        resp_sets = []

        for res in responses:
            resp_sets.append(set(res))
        
        words = {}
        
        for rs in resp_sets:
            for word in rs:
                words[word] = words.get(word, 0) + 1

        max_count = -1
        max_word = ""

        for word, count in words.items():
            if (count > max_count):
                max_word = word
                max_count = count
            elif ((count == max_count) and (word < max_word)):
                max_word = word

        return max_word
