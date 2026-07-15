

# 为高的最大矩形宽度 = (右边第一个矮子的位置) - (左边第一个矮子的位置) - 1。
class Solution:
    # def largest_rectangle_area_twice_stack(self, heights: list[int]) -> int: # 195ms
    #     len_heights = len(heights)

    #     stack = []
    #     lefts = [-1] * len_heights
    #     rights = [len_heights] * len_heights

    #     for i, height in enumerate(heights):
    #         while stack and heights[stack[-1]] >= height:
    #             stack.pop()

    #         if stack:
    #             lefts[i] = stack[-1]

    #         stack.append(i)

    #     stack.clear()

    #     for i in range(len_heights-1, -1, -1):
    #         while stack and heights[stack[-1]] >= heights[i]:
    #             stack.pop()

    #         if stack:
    #             rights[i] = stack[-1]

    #         stack.append(i)

    #     max_area = 0

    #     for i in range(len_heights):
    #         max_area = max(max_area, (rights[i] - lefts[i] - 1) * heights[i])

    #     return max_area

    # 重要思路：维护一个单调递增栈，栈中存储的是【高度的索引】。
    # 遍历高度数组，如果当前高度小于栈顶索引对应的高度，即找到了右边第一个矮子的位置，即有边界；
    # 弹出栈顶索引，把弹出的索引对应的高度作为高，计算宽度 = (右边第一个矮子的位置) - (左边第一个矮子的位置) - 1。
    # 左边第一个矮子是弹出栈后，栈顶索引对应的高度，即有边界；或者stack为空，左边界是 -1.

    # 即费曼学习法式理解：
    # 1. 维护一个单调递增栈，栈中存储的是【高度的索引】。
    # 2. 遍历高度数组，如果当前高度小于栈顶索引对应的高度，即找到了右边第一个矮子的位置，即有边界；
    # 3. 弹出栈顶索引，把弹出的索引对应的高度作为高
    # 4. 查找左边第一个矮子是：弹出栈顶索引后，栈顶索引对应的高度；或者stack为空，左边界是 -1.
    # 5. 计算宽度 = (右边第一个矮子的位置) - (左边第一个矮子的位置) - 1。
    # 6. 计算面积 = 高 * 宽，更新最大面积。

    # 【最关键思路】
    # 我维护一个单调递增栈。一旦来了个矮子（当前元素），把高个子踢飞。
    #
    # 高个子倒下的瞬间：它的高度决定了矩形的高，踢它的矮子是右边界，垫在它下面的楼是左边界
    # heights = [0] + heights + [0]，在两边加上0，保证所有的柱子都能被弹出栈计算面积。

    def largest_rectangle_area(self, heights: list[int]) -> int:  # 123ms
        heights = heights + [0]
        max_area = 0
        stack = []
        for i, height in enumerate(heights):

            while stack and heights[stack[-1]] > height:
                current_height = heights[stack.pop()]
                width = i - (stack[-1] if stack else (-1)) - 1  # 区别

                max_area = max(max_area, width * current_height)

            stack.append(i)

        return max_area

    def largest_rectangle_area_v2(self, heights: list[int]) -> int:  # 134ms
        heights = [0] + heights + [0]  # 区别
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                current_height = heights[stack.pop()]
                width = i - stack[-1] - 1  # 左开右开，所以 width = i - stack[-1] - 1

                max_area = max(max_area, width * current_height)

            stack.append(i)

        return max_area

    def largest_rectangle_area_v3(self, heights: list[int]) -> int:  # 147ms
        heights = heights + [0]
        max_area = 0
        stack = [-1]  # 区别
        for i, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > height:  # 区别
                current_height = heights[stack.pop()]
                width = i - stack[-1] - 1

                max_area = max(max_area, width * current_height)

            stack.append(i)

        return max_area


# --- 本地测试代码 ---
if __name__ == "__main__":
    sol = Solution()

    # 测试样例 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"输入: {heights1}")
    print(f"输出: {sol.largest_rectangle_area_twice_stack(heights1)}")  # 期望输出: 10
    print(f"输出: {sol.largest_rectangle_area_v2(heights1)}")  # 期望输出: 10

    # 测试样例 2
    heights2 = [2, 3, 3, 1]
    print(f"输入: {heights2}")
    print(f"输出: {sol.largest_rectangle_area_twice_stack(heights2)}")  # 期望输出: 4
    print(f"输出: {sol.largest_rectangle_area_v2(heights2)}")  # 期望输出: 4
