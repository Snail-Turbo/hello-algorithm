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

            right = -1
            max_idx = -1

            for i in range(idx, end+1):
                if right < i+nums[i]:
                    right = i+nums[i]  # 找最大可达右边，每一脚 都跳到 尽可能远
                    max_idx = i

            idx = max_idx
            ans += 1

        return ans
