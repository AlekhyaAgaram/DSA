# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        if(head is None) or (left == right):
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        

        # Move 'prev' to the node right before the 'left' position
        c = left-1
        while(c>0):
            prev = prev.next
            c -= 1

        # 'curr' will be the first node of the sub-list to reverse
        curr = prev.next

        d = right - left
        while(d):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            d -= 1

        return dummy.next


