"""
46. 全排列
已解答
中等
相关标签
premium lock icon
相关企业
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        path = []

        n = len(nums)

        used = [0] * n

        def backtrack():
            if len(path) == n:
                results.append(path[:])
                return

            for i in range(n):  # 和 01-combination 的区别，就是每个地方都遍历所有
                if used[i]:  # 然后used 不选
                    continue

                path.append(nums[i])
                used[i] = 1  # 选的同时记得 used

                backtrack()

                path.pop()
                used[i] = 0

        backtrack()

        return results


so = Solution()
nums = [1, 2, 3]
print(so.permute(nums))
