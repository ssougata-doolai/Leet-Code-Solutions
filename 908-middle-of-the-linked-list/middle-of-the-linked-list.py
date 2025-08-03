# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        flag = 0
        c = head
        d = head.next
        while d.next is not None:
            c = c.next
            d = d.next
            if d.next is None:
                flag = 1
                break
            d = d.next
        
        if flag == 1:
            return c
        else:
            return c.next
        