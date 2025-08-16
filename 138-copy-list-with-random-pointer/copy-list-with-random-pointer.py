"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        head1 = Node(0)
        temp1 = head1

        d = {}
        while temp:
            newNode = Node(temp.val)
            d[temp] = newNode
            temp1.next = newNode
            temp1 = newNode
            temp = temp.next

        temp = head
        temp1 = head1.next

        while temp:
            rand = temp.random
            if rand is None:
                temp1.random = None
            else:
                rand1 = d[rand]
                temp1.random = rand1
            temp = temp.next
            temp1 = temp1.next            
        
        return head1.next
        