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
        
        copy = {}

        current = head

        while current:
            copy[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copy[current].next = copy.get(current.next)
            copy[current].random = copy.get(current.random)
            current = current.next

        return copy[head]
        