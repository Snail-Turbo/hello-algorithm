import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, freq in freq.items():
            heapq.heappush(heap, [freq, num])

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        return [item[1] for item in heap]


test = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
so = Solution()
print(so.topKFrequent(test, 4))
