from typing import List, Optional
import sys
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # 关键思路：
        # 1. 使用最小堆（优先队列）来存储每个链表的当前节点。
        # 2. 每次从堆中取出最小的节点，并将其加入到结果链表中。
        # 3. 如果取出的节点有下一个节点，则将下一个节点加入堆中。
        #
        # 注意事项：
        # 1. 需要在堆中存储节点的值、链表索引和节点本身，以避免在值相同的情况下比较 ListNode 对象。
        # 2. 使用一个哑节点（dummy node）来简化结果链表的构建过程。
        # 3. 时间复杂度为 O(N log k)，其中 N 是所有链表中节点的总数，k 是链表的数量。每个节点都会被插入和弹出堆一次，堆的大小最多为 k。
        # 4. 空间复杂度为 O(k)，用于存储堆中的节点。

        tmp_heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(tmp_heap, (head.val, i, head))  # 如果 head1.val = head2.val，则会对比下一个，但是 ListNode是不含 对比 __lt__ 的

        dummy = ListNode()
        current = dummy
        while tmp_heap:
            _, i, current_tmp_node = heapq.heappop(tmp_heap)

            current.next = current_tmp_node

            current = current.next

            if current_tmp_node.next:
                heapq.heappush(tmp_heap, (current_tmp_node.next.val, i, current_tmp_node.next))

        return dummy.next
