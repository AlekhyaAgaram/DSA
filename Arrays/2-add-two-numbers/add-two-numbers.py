# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = ListNode(0)
        q = head

        while(l1 or l2 or (carry != 0)):

            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0

            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
        
            tval = v1 + v2 + carry
            
            carry = tval // 10
            temp = ListNode(tval % 10)

            q.next = temp
            q = temp

        return head.next
        