# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        q = head
        prev = head
        c = n
        while(c!=0):
            q = q.next
            c-=1

        if q is None:
            return head.next
        
        while(q.next is not None):
            prev = prev.next
            q = q.next

        temp = prev.next
        prev.next = temp.next

        return head
