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
        if not head:
            return None

        new_nodes = {}

        temp = head
        while temp:
            new_node = Node(temp.val, temp.next)
            new_nodes[temp] = new_node
            temp = temp.next
        
        temp = head
        new_ll = new_nodes[head]
        new_temp = new_ll
        while temp and temp.next:
            new_temp.next = new_nodes[temp.next]
            temp = temp.next
            new_temp = new_temp.next
        

        temp = head
        new_temp = new_ll
        while new_temp:
            if temp.random:
                new_temp.random = new_nodes[temp.random]
            else:
                new_temp.random = None
            temp = temp.next
            new_temp = new_temp.next

        return new_ll

