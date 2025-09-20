# LeetCode #0206 | Reverse Linked List | [EASY]
# [!] IMPORTANT (Linked List)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous = None
        current = head

        while current is not None:
            remember = current.next
            current.next = previous
            previous = current
            current = remember
        
        return previous