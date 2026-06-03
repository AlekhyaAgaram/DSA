# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        p = head
       

        while(p!=None):
            q = p.next
            if q and (p.val == q.val):
                while q and  p.val == q.val:
                    q = q.next
                prev.next = q
                p = q
            else:
                # No duplicates found for 'p', move both pointers forward
                prev = p
                p = p.next
                
        return dummy.next