from typing import Optional
import sys
import re


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        current_1 = l1
        current_2 = l2

        while current_1 or current_2 or carry:
            a = current_1.val if current_1 else 0
            b = current_2.val if current_2 else 0
            current_sum = a + b + carry

            carry = current_sum // 10

            current.next = ListNode(current_sum % 10, None)
            current = current.next

            if current_1:
                current_1 = current_1.next

            if current_2:
                current_2 = current_2.next

        return dummy.next
