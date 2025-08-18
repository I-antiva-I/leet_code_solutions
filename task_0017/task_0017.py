# LeetCode #0017 | Letter Combinations of a Phone Number | [MEDIUM]

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" :
            return []

        combo = ""
        letters = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }
        combos = []

        def makeCombo(combo):
            if len(combo) == len(digits):
                combos.append(combo)
            else:
                for char in letters[digits[len(combo)]]:
                    makeCombo(combo+char)

        makeCombo(combo)
        return combos