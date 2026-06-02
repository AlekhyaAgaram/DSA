"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0)
        q = dummy
        p = head
        d = {}

        while(p!=None):
            # copy value and create copy node q
            temp = Node(p.val)
            q.next = temp
            q = q.next

            #map original node and copy node
            d[p] = q

            #move orginial list
            p = p.next

        a = dummy.next
        b = head
        while(b!=None):
            if(b.random):
                a.random = d[b.random]
            a = a.next
            b = b.next


        return dummy.next


