# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        temp = head
        if count == 1:
            return None
        if count == n:
            return head.next
        l = count - n - 1
        for i in range(l):
            temp = temp.next

        temp.next = temp.next.next
        return head