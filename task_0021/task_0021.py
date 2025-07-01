# LeetCode #0021

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a root node, to which other nodes will be attached.
        head = ListNode()
        tail = head

        # Iterate through list1 and list2.
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach remaining nodes.
        if list1 != None:
            tail.next = list1
        if list2 != None:
            tail.next = list2

        return head.next