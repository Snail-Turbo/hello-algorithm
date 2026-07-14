# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current_A = list1
        current_B = list2

        # 【重要】
        virtual_node = ListNode()  # 虚拟头节点，减少一些处理逻辑

        current_node = virtual_node

        while current_A and current_B:
            if current_A.val < current_B.val:
                current_node.next = current_A

                current_A = current_A.next
            else:
                current_node.next = current_B

                current_B = current_B.next

            current_node = current_node.next

        # 还剩的直接接上
        if current_A:
            current_node.next = current_A
        else:
            current_node.next = current_B

        # 【重要】 这里 return 是 virtual_node.next
        return virtual_node.next
