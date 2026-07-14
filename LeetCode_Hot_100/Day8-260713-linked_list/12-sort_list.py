from typing import Optional
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # return sorted_head
        if not head or not head.next:
            return head

        slow: ListNode = head
        fast: ListNode = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 if l1 else l2

        return dummy.next
