# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = head
        b = head

        while b.next and b.next.next:
            a = a.next
            b = b.next.next
        
        cur = a.next
        a.next = None

        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        cur = head
        while pre:
            tmp1 = cur.next
            tmp2 = pre.next
            pre.next = cur.next
            cur.next = pre
            cur = tmp1
            pre = tmp2