# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp1 = head

        # Edge cases
        if temp1 is None or temp1.next is None:
            return head
        if k == 0:
            return head

        count = 0
        # length of the linked list
        while temp1:
            count += 1
            temp1 = temp1.next

        # push the pointer to k position
        k = k % count
        temp1 = head
        for i in range(k):
            temp1 = temp1.next
            if temp1 is None:
                temp1 = head

        # finding the head
        temp2 = head
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next

        temp1.next = head
        head = temp2.next
        temp2.next = None

        return head


        
        