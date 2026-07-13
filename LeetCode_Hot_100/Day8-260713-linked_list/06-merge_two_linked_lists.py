# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current_A = list1
        current_B = list2

        virtual_node = ListNode()  # 虚拟头节点，减少一些处理逻辑
        result = virtual_node

        while current_A and current_B:
            if current_A.val < current_B.val:
                result.next = current_A

                current_A = current_A.next
            else:
                result.next = current_B

                current_B = current_B.next

            result = result.next

        if current_A:
            result.next = current_A
        else:
            result.next = current_B

        return result.next
