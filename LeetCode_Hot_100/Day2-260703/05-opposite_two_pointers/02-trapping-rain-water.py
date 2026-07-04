"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
"""

# 关键思路：【移动矮的那一边，因为右边能够兜住】
# 1. 使用双指针法，从数组的两端开始，逐步向中间移动。
# 2. 每次计算当前指针所指的两条线形成的容器的面积，并更新最大面积。
# 3. 移动较短的那条线的指针，因为移动较高的线不会增加面积。

# 
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        i, j = 0, n-1
        max_left = max_right = 0

        answer = 0

        while i < j:
            # 先走可能漏水的那一边，因为另一边高，能兜住
            if height[i] < height[j]:
                if height[i] < max_left:
                    answer += max_left - height[i]
                else:
                    max_left = height[i]
                
                i += 1
            else:
                if height[j] < max_right:
                    answer += max_right - height[j] # 右边向左走，右边有已经遍历过的更高，所以右边能兜住
                else:
                    max_right = height[j]
                
                j -= 1

        return answer


        # n = len(height)

        # left_idx, right_idx = 0, n-1

        # max_left, max_right = 0, 0

        # answer = 0

        # while left_idx < right_idx:
        #     max_left = max(max_left, height[left_idx])
        #     max_right = max(max_right, height[right_idx])

        #     if height[left_idx] < height[right_idx]:
        #         answer += max_left - height[left_idx]
        #         left_idx += 1
        #     else:
        #         answer += max_right - height[right_idx]
        #         right_idx -= 1 # 【重要犯错】 右边的指针的idx是往左减少的


        # return answer
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
so = Solution()
print(so.trap(height))