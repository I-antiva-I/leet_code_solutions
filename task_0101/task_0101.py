# LeetCode #0101 | Symmetric Tree | [EASY]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def is_mirrored(self, left, right):
       if (left == None) and (right == None):
           return True

       if (left == None) or (right == None):
           return False

       if left.val == right.val:
           return self.is_mirrored(left.left, right.right) and self.is_mirrored(left.right, right.left)  
       else:
           return False

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.is_mirrored(root.left, root.right)