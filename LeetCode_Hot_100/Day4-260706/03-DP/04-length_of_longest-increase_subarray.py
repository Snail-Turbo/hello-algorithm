class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 个人思路：试试从后往前走，以当前nums[index]作为连续数组的开始

        # nums = [0, 1, 0, 3, 2, 3]
        # len_nums = 6
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        dp = [0] * (len(nums)+1)  # len_dp = 7

        dp[-1] = 0  # len(nums) = len_dp - 1 = 6
        dp[-2] = 1  # len(nums)-1 = len_dp -2 = 5

        max_length = 0

        min_impossible = -10001
        nums.append(min_impossible)
        # nums = [0, 1, 0, 3, 2, 3, -INF]

        for i in range(len(dp)-3, -1, -1):
            dp[i] = max([dp[j]+1 for j in range(i+1, len(dp)-1) if nums[j] > nums[i]], 1)

            if max_length < dp[i]:
                max_length = dp[i]

            # dp[4]
        # dp[i] = max(dp_post + 1 for dp_post in dp[i+1:] if nums[i])

        # dp[i] = max(dp[j]+1 for j in range(i+1, len(nums)) if nums[j]<nums[i])
        # dp[8] = 0
        # dp[7] = 1
        # dp[6] = 1
        # dp[5] = 2
        # dp[4] = 3

        return max_length

    def lengthOfLIS_2(self, nums: list[int]) -> int:
        n = len(nums)
        if not nums or n == 0:
            return 0

        dp = [1] * n  # 优化初始化

        max_length = dp[n-1]  # 优化初始化

        for i in range(n-2, -1, -1):
            for j in range(i+1, len(dp)):  # 减少多次list创建
                if nums[j] > nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j]+1

            if max_length < dp[i]:
                max_length = dp[i]

        return max_length

    def lengthOfLIS_3(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(n):  # 先遍历 end_index
            for j in range(i):  # 然后遍历  j in range(end_index)
                if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1

        ans = max(dp)

        return ans


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums2 = [0, 1, 0, 3, 2, 3]
nums3 = []
so = Solution()
print(so.lengthOfLIS(nums))
print(so.lengthOfLIS(nums2))
print(so.lengthOfLIS(nums3))
