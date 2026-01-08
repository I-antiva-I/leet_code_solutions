# LeetCode #2325 | Decode the Message | [EASY]

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        
        key_char = {' ' : 32}
        result = ""
        
        for k in key:
            if k not in key_char:
                key_char[k] = len(key_char)+96
        
        for m in message:
            result += chr(key_char[m])

        return result