# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(curr,k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. Check if there are at least k nodes left
            kth = getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # 2. Reverse the k nodes
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Connect previous group to the new head
            # group_prev.next is the old head (now the tail)
            old_head = group_prev.next
            group_prev.next = kth
            group_prev = old_head

        return dummy.next