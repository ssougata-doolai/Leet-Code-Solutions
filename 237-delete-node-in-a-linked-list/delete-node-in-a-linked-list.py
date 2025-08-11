# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        temp = node
        node = node.next
        while node.next is not None:
            temp.val = node.val
            node = node.next
            temp = temp.next
        
        temp.val = node.val
        temp.next = None

        