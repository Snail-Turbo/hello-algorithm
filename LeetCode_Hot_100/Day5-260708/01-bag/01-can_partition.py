"""
416. 分割等和子集


给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_total = sum(nums)
        if sum_total % 2 != 0:
            return False

        target = sum_total // 2
        dp = [[False] * (target+1) for _ in range(len(nums)+1)]

        dp[0][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                current_num = nums[i-1]
                dp[i][j] = dp[i-1][j] or (dp[i-1][j-current_num] if j-current_num >= 0 else False)

        return dp[-1][-1]

    # 【额外思路】：
    # 又因为 dp[i][j] = dp[i-1][j] or dp[i-1][j-num（if ok）]
    # 所以 依赖 j 和 j-num
    # 倒叙就可以用上j，j位置就可以释放了，j-num还在存


input_nums = [100, 4, 6]
so = Solution()
print(so.canPartition(input_nums))
