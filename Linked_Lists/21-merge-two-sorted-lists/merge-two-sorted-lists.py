# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        q = dummy

        while(list1 and list2):
            if(list1.val <= list2.val):
                q.next = list1
                list1 = list1.next
            else:
                q.next = list2
                list2 = list2.next
            q = q.next

        if list1:
            q.next = list1
        else:
            q.next = list2
        return dummy.next