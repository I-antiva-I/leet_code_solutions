# LeetCode #0049 | Group Anagrams | [MEDIUM]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        
        return groups.values()