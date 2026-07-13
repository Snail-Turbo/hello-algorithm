from typing import Optional
import sys
import re


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd_recursive(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        target = n
        prefix_node: ListNode = None
        result_head = head

        def dfs(current_node: ListNode):
            nonlocal count
            nonlocal prefix_node

            if current_node is None:  # 上一次的 current_node 为最后一个
                return True

            if not dfs(current_node.next):
                return False

            count += 1
            if count == target + 1:  # 这里是找 要删除的 节点的 上一个节点
                prefix_node = current_node

            return True  # 【易错点】这里必须是True，否则回溯到倒数第二个就停了

        dfs(result_head)

        if prefix_node is not None:
            prefix_node.next = prefix_node.next.next
            return result_head

        return head.next  # 如果没有 prefix_node，说明 要删除的就是第一个

    def removeNthFromEn_two_pointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()  # dummy 使得一定能够走 n+1
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n + 1):  # n + 1 使得 fast 到 None 的时候，slow 在 previous
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
