# LeetCode #0482 | License Key Formatting | [EASY] |

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        line = s.replace("-","").upper()
        size = len(line)
        first_group = size % k or k
        groups = [line[:first_group]]

        for i in range(first_group, size, k):
            groups.append(line[i:i+k])

        return "-".join(groups)
