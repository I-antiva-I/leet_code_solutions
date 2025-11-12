# LeetCode #3024 | Type of Triangle | [EASY]

class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # (?) Triangle inequality theorem
        if ((nums[0]+nums[1] > nums[2]) and (nums[0]+nums[2] > nums[1]) and (nums[2]+nums[1] > nums[0])):
            
            if ((nums[0] == nums[1]) and (nums[0] == nums[2])):
                return "equilateral"

            elif ((nums[0] == nums[1]) or (nums[0] == nums[2]) or (nums[1] == nums[2])):
                return "isosceles"

            else:
                return "scalene"
        
        else:
            return "none"
        