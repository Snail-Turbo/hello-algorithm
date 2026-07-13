# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x

        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        already = set()

        current = headA

        while current:
            already.add(current)  # 这里 add 的必须是 current_node
            current = current.next

        current = headB

        while current:
            if current in already:
                return current

            current = current.next

        return None
