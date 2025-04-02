# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        cur = head

        while cur is not None:
            cur_next = cur.next
            cur.next = before
            before = cur
            
            cur = cur_next
        
        return before
        