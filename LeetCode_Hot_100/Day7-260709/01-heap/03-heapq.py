import heapq

heap = []


nums = [3, 1, 2, 4]

for num in nums:
    heapq.heappush(heap, num)


top_x = heap[0]

# pop
top_x = heapq.heappop(heap)

nums_2 = [3, 1, 2, 4]
heapq.heapify(nums_2)
