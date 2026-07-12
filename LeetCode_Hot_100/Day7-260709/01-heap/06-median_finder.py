"""
295. 数据流的中位数

中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10**(-5) 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:

-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian


5
1 2

4
7 8
9


"""

import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.left_heap = []   # max, in positive
        self.right_heap = []  # min, in real

    def addNum(self, num: int) -> None:
        if self.right_heap and num >= self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)

        if len(self.right_heap) > len(self.left_heap) + 1:
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        elif len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))  # 负号 在结果的前面

    def findMedian(self) -> float:
        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]

        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]

        return (-self.left_heap[0] + self.right_heap[0])/2


def main() -> None:
    q = int(input())
    mf = MedianFinder()
    for _ in range(q):
        parts = input().split()
        if parts[0] == "add":
            mf.addNum(int(parts[1]))
        else:
            print(f"{mf.findMedian():.1f}")


if __name__ == "__main__":
    main()
