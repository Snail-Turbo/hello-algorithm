from typing import Optional
import sys


class Node:
    def __init__(self, val: int = 0, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new_map = {}
        current = head
        while current:
            old_to_new_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            old_to_new_map[current].next = old_to_new_map.get(current.next)  # 这里要用 get，因为 next，random 可能是 None
            old_to_new_map[current].random = old_to_new_map.get(current.random)
            current = current.next

        return old_to_new_map[head]
