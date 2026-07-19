# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head

        values = []

        while current:
            values.append(current.val)
            current = current.next

        left, right = 0, len(values)-1

        while left < right:
            if values[left] != values[right]:
                return False

            left += 1
            right -= 1

        return True

    def isPalindrome_recursive(self, head: ListNode) -> bool:
        front = head

        def check_back(current: ListNode) -> bool:
            nonlocal front

            if not current:  # 到最后的时候，current.next = None
                return True

            if not check_back(current.next):  # 压倒
                return False

            if front.val != current.val:
                return False

            front = front.next
            return True

        return check_back(head)

    # 快慢双指针 + reverse:

    # 1 -> 2 -> 3
    # 会变成：
    # 1 -> 2 <- 3

    # 1，2，3，4
    # 会变成
    # 1 -> 2 -> 3 <- 4
    def _reverse_linked_list(self, head: ListNode) -> ListNode:
        already = None
        current = head

        while current:
            next = current.next
            current.next = already  # 如果是奇数个，这里会是中间多的那个，这使得如果123，则2.next = None

            already = current

            current = next

        return already

    def isPalindrome_sliding_window(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = self._reverse_linked_list(slow)
        first = head

        while second:  # 这里必须以 second为准，因为没有切断前面
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
