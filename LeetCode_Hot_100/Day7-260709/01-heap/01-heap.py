
import heapq
"""
重要性质：堆顶是集合最小值

1.根据局部有序性，考虑从根节点开始往下走到任意一个节点，整个过程值是非递减的，也就是数值会越来越大。

2.又因为根节点能到达所有其他节点。

根节点的值小于等于所有其他节点的值，即根节点的值是全局最小值。

所以牢记一点，对堆的任何操作，我们一定要确保操作完后堆的性质不要被破坏。因为只要破环了，我们就无法再获得全局最小值了！
"""


class my_heap:

    def __init__(self):
        self.heap: list = []
        self.size = 0

    def push(self, value):
        self.heap.append(value)

        self.size += 1

        self._heapify_up(self.size - 1)

    def pop(self):
        if self.size == 0:
            return None

        # 这里交换：为了 用 -1 位置 存储 last top，这样用于 return，不用额外开一个内存空间
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.size -= 1
        self._heapify_down(0)

        return self.heap.pop()

    def _heapify_up(self, target_index):
        parent_index = (target_index - 1) // 2

        if parent_index >= 0 and self.heap[parent_index] > self.heap[target_index]:
            self.heap[parent_index], self.heap[target_index] = self.heap[target_index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, target_index):

        left_index = 2 * target_index + 1
        right_index = 2 * target_index + 2

        min_index = target_index
        if left_index < self.size and self.heap[left_index] < self.heap[min_index]:
            min_index = left_index

        if right_index < self.size and self.heap[right_index] < self.heap[min_index]:
            min_index = right_index

        if min_index != target_index:
            self.heap[min_index], self.heap[target_index] = self.heap[target_index], self.heap[min_index]
            self._heapify_down(min_index)
