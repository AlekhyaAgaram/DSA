# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less_head = ListNode(0)
        great_head = ListNode(0)

        less = less_head
        great = great_head
        curr = head
        dummy = less.next

        while(curr !=None):
            if curr.val >= x:
                great.next = curr
                great = great.next
            else:
                less.next = curr
                less = less.next
            curr = curr.next
        great.next = None
        less.next = great_head.next

        return less_head.next

