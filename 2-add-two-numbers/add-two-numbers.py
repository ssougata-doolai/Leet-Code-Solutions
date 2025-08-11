# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp3 = ListNode()
        temp1 = l1
        temp2 = l2
        l3 = temp3

        c = 0
        while temp1 and temp2:
            s1 = temp1.val + temp2.val + c
            c = s1 // 10
            s = s1 % 10
            new_node = ListNode(s)
            temp3.next = new_node
            temp3 = temp3.next
            temp2 = temp2.next
            temp1 = temp1.next
            
        while temp1 is not None:
            s = (temp1.val + c) % 10
            c = (temp1.val + c) // 10
            new_node = ListNode(s)
            temp3.next = new_node
            temp3 = temp3.next
            temp1 = temp1.next

        while temp2 is not None:
            s = (temp2.val + c) % 10
            c = (temp2.val + c) // 10
            new_node = ListNode(s)
            temp3.next = new_node
            temp3 = temp3.next
            temp2 = temp2.next
        
        if c != 0:
            temp3.next = ListNode(c)

        return l3.next


        