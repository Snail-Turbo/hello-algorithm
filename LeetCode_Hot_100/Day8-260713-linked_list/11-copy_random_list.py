from typing import Optional
import sys


class Node:
    def __init__(self, val: int = 0, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    # 关键思路：
    # 1. 先遍历一遍链表，建立原节点到新节点的映射关系。
    # 2. 再遍历一遍链表，利用映射关系建立新节点的 next 和 random 指针。
    # 2内的注意事项：
    #  - 这里要用 get，因为 next，random 可能是 None
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
            old_to_new_map[current].next = old_to_new_map.get(current.next, None)  # 这里要用 get，因为 next，random 可能是 None
            old_to_new_map[current].random = old_to_new_map.get(current.random, None)
            current = current.next

        return old_to_new_map[head]
