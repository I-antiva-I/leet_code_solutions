# LeetCode #0915 | Partition Array into Disjoint Intervals | [MEDIUM] |

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left_max = nums[0]
        global_max = nums[0]
        split_index = 0

        for i in range(1, len(nums)):
            global_max = max(global_max, nums[i])

            if nums[i] < left_max:
                split_index = i
                left_max = global_max

        return split_index+1