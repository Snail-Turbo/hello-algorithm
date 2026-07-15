# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        visited = set()

        current = head

        i = 0

        while current:
            if current in visited:
                return current

            visited.add(current)
            i += 1

            current = current.next

        return None

    def detectCycle_slow_fast_pointer(self, head: ListNode) -> ListNode:
        # 2b - b = k * c：
        # 即 b = k*c
        # 多走的：b - a = k*c - a

        # 即：相遇点再走 a 步，就是走了 k 周

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head  # head 走 a 步会到 环起点
                # 原来的 slow 现在的位置，走 a 步 正好就是 kc，也就回到起点

                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow

        # slow is None
        # slow.next is None
        # if slow != fast or slow is None or slow.next is None:
        return None
