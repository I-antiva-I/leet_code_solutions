# LeetCode #1909 | Remove One Element to Make the Array Strictly Increasing | [EASY] |

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        item_removed = False
        index = 1
        n = len(nums)

        while(index < n):
            if (nums[index] <= nums[index-1]):
                if (item_removed):
                    return False
                else:               
                    before_prev_item = -1 if index - 2 < 0 else nums[index-2]
                    next_item = 1001 if index + 1 == n else nums[index+1]

                    if (nums[index-1] >= next_item):
                        nums[index-1] = before_prev_item
                        index -= 1
                    else:
                        nums[index] = nums[index-1]
                    
                    item_removed = True
            
            index += 1
        
        return True
