
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, value: int):
        self.heap.append(value)
        self.size += 1

        self._heapify_up(self.size - 1)

    def pop(self) -> int:
        if self.size == 0:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.size -= 1

        if self.size > 0:
            self._heapify_down(0)

        return self.heap.pop()

    def _heapify_up(self, target_index):

        while target_index > 0:
            parent_index = (target_index - 1)//2

            if self.heap[parent_index] <= self.heap[target_index]:
                break

            self.heap[target_index], self.heap[parent_index] = self.heap[parent_index], self.heap[target_index]
            target_index = parent_index

    def _heapify_down(self, target_index):

        while True:
            min_index = target_index

            left_index = 2 * target_index + 1
            right_index = 2 * target_index + 2

            if left_index < self.size and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index

            if right_index < self.size and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index

            if min_index == target_index:
                break

            self.heap[min_index], self.heap[target_index] = self.heap[target_index], self.heap[min_index]
            target_index = min_index


def heap_sort(array: list[int]) -> list[int]:
    min_heap = MinHeap()

    for num in array:
        min_heap.push(num)

    answers = []

    while min_heap.size > 0:
        answers.append(min_heap.pop())

    return answers
