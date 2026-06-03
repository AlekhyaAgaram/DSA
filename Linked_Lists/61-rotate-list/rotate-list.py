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
        if not head or not head.next or k == 0:
            return head
    
        q = head
        length = 1
        while(q.next!= None):
            p = q
            q = q.next
            length += 1

        #if k > length
        k = k % length
        if k == 0:
            return head


        q.next = head
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
            
        # node after the new tail is the new head
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head

