# LeetCode #3582 | Generate Tag for Video Caption | [EASY] |

class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        
        tag = "#"
        limit = 99
        words = caption.split()

        if (not words):
            return tag
  
        w_len = len(words[0])
        tag = tag + words[0][:min(w_len, limit)].lower()
        limit -= w_len

        for w in words[1:]:
            if (limit <= 0):
                break

            w_len = len(w)
            tag = tag + w[:min(w_len, limit)].capitalize()
            limit -= w_len

        return tag
            