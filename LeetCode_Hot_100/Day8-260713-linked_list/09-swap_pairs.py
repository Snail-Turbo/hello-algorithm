from typing import Optional
import sys


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        dummy.next = head

        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first
            previous.next = second

            previous = first

        return dummy.next
