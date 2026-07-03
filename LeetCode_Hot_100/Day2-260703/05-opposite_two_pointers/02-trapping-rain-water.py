"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_idx, right_idx = 0, n-1

        max_left, max_right = 0, 0

        answer = 0

        while left_idx < right_idx:
            max_left = max(max_left, height[left_idx])
            max_right = max(max_right, height[right_idx])

            if height[left_idx] < height[right_idx]:
                answer += max_left - height[left_idx]
                left_idx += 1
            else:
                answer += max_right - height[right_idx]
                right_idx -= 1 # 【重要犯错】 右边的指针的idx是往左减少的


        return answer
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
so = Solution()
print(so.trap(height))