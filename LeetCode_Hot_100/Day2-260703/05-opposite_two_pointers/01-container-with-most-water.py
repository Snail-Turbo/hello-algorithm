"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

 
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
"""

# 思路：
# 1. 使用双指针法，从数组的两端开始，逐步向中间移动。
# 2. 每次计算当前指针所指的两条线形成的容器的面积，并更新最大面积。
# 3. 移动较短的那条线的指针，因为移动较高的线不会增加面积。
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_area = 0

        i, j = 0, n - 1
        while i < j:
            area = (j - i) * min(height[i], height[j]) # j-i 而不是 j-i+1，因为 j-i 是两条线之间的距离，min(height[i], height[j]) 是容器的高度
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


        
    

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))  # 输出: 49