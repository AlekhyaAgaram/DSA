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
            if(list1.val < list2.val):
                t = list1.val
                list1 = list1.next
            else:
                t = list2.val
                list2 = list2.next

            temp = ListNode(t)
            q.next = temp
            q = q.next

        if list1:
            q.next = list1
            q = q.next
        elif list2:
            q.next = list2
            q = q.next
        return dummy.next