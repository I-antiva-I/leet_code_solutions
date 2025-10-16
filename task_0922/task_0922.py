# LeetCode #0922 | Sort Array By Parity II | [EASY] |

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        odd = 1
        even = 0

        while( odd < len(nums) ):

            if (nums[odd] % 2 == 1):
                odd += 2
                continue
            if (nums[even] % 2 == 0):
                even += 2
                continue

            nums[even], nums[odd] = nums[odd], nums[even]
            odd += 2
            even += 2
        
        return nums