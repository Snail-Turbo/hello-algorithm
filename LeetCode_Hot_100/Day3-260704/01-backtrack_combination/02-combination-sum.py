"""
39. 组合总和
中等
相关标签
premium lock icon
相关企业
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        results, path = [], []  # 这里尽量不要偷懒，连等就是 引用

        def backtrack(current_idx, current_sum):
            if current_sum > target:  # 有终止条件
                return

            if current_sum == target:  # 有记录条件
                results.append(path[:])
                return

            for i in range(current_idx, len(candidates)):
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i])  # 无限制重复被选取

                path.pop()

        backtrack(0, 0)  # 【永远别忘了开始！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！】

        return results

    def combinationSum_ols(self, candidates: list[int], target: int) -> list[list[int]]:
        # 【完全背包思想】：
        # 一次性穷举它所有可能的使用次数，然后坚决走向下一个数字
        # 坚决的 index 走到 len(candidates)，即使已经 5个2确认后面都不选了

        ans = []

        def dfs(index, total, candidates, curr):
            if index == len(candidates):
                if total == target:  # 如果当前总和等于目标值，添加当前组合到结果列表
                    ans.append(curr)
                return

            rest = target - total  # 计算剩余的目标值
            up = rest // candidates[index]  # 一次性穷举它所有可能的使用次数，然后坚决走向下一个数字

            for i in range(up + 1):  # 从 0 到 up 次使用当前候选数
                dfs(index + 1, total + i * candidates[index], candidates, curr + [candidates[index]] * i)

        dfs(0, 0, candidates, [])  # 从索引 0 开始，初始总和为 0，当前组合为空 # 【永远别忘了开始！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！】
        return ans

    def combinationSum_if(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(index, current_sum, path):
            if index == len(candidates):  # 终止条件就终止，他也是满足条件之一
                if current_sum == target:  # 满足条件另一
                    result.append(path[:])
                return

            dfs(index + 1, current_sum, path)

            if current_sum + candidates[index] <= target:
                dfs(index, current_sum + candidates[index], path + [candidates[index]])

        dfs(0, 0, [])  # 【永远别忘了开始！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！】

        return result


candidates = [2, 3, 6, 7]
target = 12
so = Solution()
print(so.combinationSum(candidates, target))
print(so.combinationSum_if(candidates, target))
