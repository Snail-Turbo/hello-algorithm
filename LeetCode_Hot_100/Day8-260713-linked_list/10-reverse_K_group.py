from typing import Optional
import sys
import re


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def _reverse_linked_list(self, previous_node, first_head: ListNode, target_count):
    #     already = None
    #     current: ListNode = head

    #     count = 0
    #     while current:
    #         tmp_next = current.next
    #         current.next = already
    #         already = current

    #         current = tmp_next
    #         count += 1

    #         if count == target_count:
    #             head.next = current
    #             break

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 思路：
        # 1. 快慢双指针，快 从 dummy 走 k 到 current_stage_last：若走不到 k 则 return dummy.next (已结束)
        # 2. group_previous = dummy
        #
        # 3. next_first = current_stage_last.next
        # 4. already = next_first
        #
        # 5. 从 current = group_previous.next 开始 包含在内的 k 个
        # a. tmp_next = current.next
        # b. current.next = already
        # c. already = current
        # d. current = tmp_next
        #
        # 6. next_group_previous = group_previous.next
        # 7. group_previous.next = already
        # 8. group_previous = next_group_previous

        dummy = ListNode(0, head)

        group_previous = dummy

        while group_previous and group_previous.next:
            fast = group_previous
            for _ in range(k):
                fast = fast.next
                if fast is None:
                    return dummy.next

            already = fast.next
            current = group_previous.next

            for _ in range(k):
                tmp_next = current.next
                current.next = already

                already = current
                current = tmp_next

            next_group_previous = group_previous.next
            group_previous.next = already

            group_previous = next_group_previous

        return dummy.next
