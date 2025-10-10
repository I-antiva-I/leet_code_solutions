# LeetCode #0914 | X of a Kind in a Deck of Cards | [EASY] |
# [!] IMPORTANT (Greatest Common Divisor)

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        numbers = {}

        for num in deck:
            numbers[num] = numbers.get(num, 0) + 1

        possible_combination = min(numbers.values())
        if (possible_combination == 1):
            return False

        def find_gcd(a, b):
            if (a == 0):
                return b
            return find_gcd(b % a, a)

        for num in numbers.values():
            possible_combination = find_gcd(possible_combination, num)
        
        return (possible_combination != 1)