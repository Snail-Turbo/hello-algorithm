class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        ans = 0
        end = 0
        idx = 0

        while end < n-1:
            current_num = nums[idx]

            end = min(idx+current_num, n-1)

            current_right = -1
            max_idx = -1

            for i in range(idx, end+1):  # 处理i位置，i 到 i+nums[i]（end） 之间的位置，这之间 哪个能跳到最远，就去哪个
                if current_right < i+nums[i]:
                    current_right = i+nums[i]  # 找最大可达右边，每一脚 都跳到 尽可能远
                    max_idx = i

            idx = max_idx
            ans += 1

        return ans

    def jump2(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        ans = 0
        end = 0
        right = 0
        for i in range(n-1):
            right = max(right, i+nums[i])

            if i == end:
                ans += 1
                end = right
            # 如果跳到一次 end，就是结束一次

        return ans
