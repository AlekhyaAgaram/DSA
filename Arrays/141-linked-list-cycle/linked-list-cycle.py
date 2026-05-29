# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = head
        s = set()

        while(q!= None):
            if(q not in s):
                s.add(q)  
                q = q.next
            else:
                return True
        return False  
        