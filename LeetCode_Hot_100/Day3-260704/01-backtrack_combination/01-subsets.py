"""
78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同


当前题，最简单的 【无限制回溯类型题】
思路：
1. 2叉树的回溯法
2. N叉树的回溯法（无限制，全都append的for循环形式）
"""


class Solution:
    # 当前题，最简单的 【无限制回溯】

    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 2叉树的回溯法

        result = []  # 用来存储结果
        current_subset = []  # 当前的正在构造的 子集 状态

        n = len(nums)

        def dfs(index):
            if index == n:
                result.append(current_subset[:])
                return

            current_subset.append(nums[index])
            dfs(index + 1)

            current_subset.pop()
            dfs(index+1)

        dfs(0)

        return result

    def subsets_for(self, nums: list[int]) -> list[list[int]]:
        # N = len(nums)
        # N叉树的回溯法

        result = []
        path = []

        def backtrack(current_index):
            result.append(path[:])

            for i in range(current_index, len(nums)):
                path.append(nums[i])
                backtrack(i+1)  # 【一个进阶】：不可重复选择，就往下走，可重复选择就是i

                path.pop()

        backtrack(0)

        return result

    def subsets_for_each(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)

        results = []
        path = []

        def backtrack(current_index):
            results.append(path[:])  # 必须是 path[:] 拷贝！不能直接传 path

            for i in range(current_index, n):  # current_index 的作用就是 used
                path.append(nums[i])

                backtrack(i + 1)
                # backtrack(i)

                path.pop()

        backtrack(0)  # 千万别忘了启动！

        return results


nums = [1, 2, 3]

so = Solution()
print(so.subsets_for(nums))
