# LeetCode #2591 | Distribute Money to Maximum Children | [EASY] |

class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        
        if (children > money):
            return -1
        else:
            # Give all one dollar
            free_money = money - children
            children_with_8 = min(free_money // 7, children)
            children_with_1 = children - children_with_8
            free_money = free_money - 7 * children_with_8

            if (((children_with_1 == 1) and (free_money == 3)) or ((children_with_1 == 0) and (free_money != 0))):
                return children_with_8 - 1
            else: 
                return children_with_8
        