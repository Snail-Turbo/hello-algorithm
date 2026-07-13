# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        current = head
        already = None

        while current:
            next_node: ListNode = current.next  # 先把马上要覆盖的存下来

            current.next = already  # 当前的 next 一定是 already

            already = current

            current = next_node

        return already
