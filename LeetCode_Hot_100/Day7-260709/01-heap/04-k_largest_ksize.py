from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(num)

            if len(heap) > k:
                heapq.heappop(num)

        return heap[0]
