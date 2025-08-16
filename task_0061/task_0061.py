# LeetCode #0061 | Rotate List | [MEDIUM]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head == None or k == 0:
            return head

        # Connect list.
        size = 1
        tail = head
        while(tail.next != None):
            tail = tail.next
            size += 1
        tail.next = head

        # Find new tail and disconnect list.
        nodes_to_skip = size - (k % size) - 1
        tail = head
        for i in range(nodes_to_skip):
            tail = tail.next
        new_head = tail.next 
        tail.next = None

        return new_head