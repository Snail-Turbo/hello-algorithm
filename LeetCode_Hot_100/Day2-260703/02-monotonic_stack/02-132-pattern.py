

class Solution:
    def find_132_pattern(self, nums: list[int]) -> bool:

        n = len(nums)
        if n < 3:
            return False

        mins = [0] * n  # 这里只需要开辟即可，因为 mins[i] = min(mins[i-1], nums[i])
        mins[0] = nums[0]

        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])

        # 单调栈（递减），存储的是候选 j 的索引
        index_stack = []
        for k in range(n):
            # 弹出栈中 ≤ nums[k] 的元素，保证栈是单调递减的
            while index_stack and nums[index_stack[-1]] <= nums[k]:
                index_stack.pop()

            # 若栈非空，栈顶是 nums[k] 左边第一个比它大的元素 → 候选的 nums[j]
            # 检查该 j 之前的最小值（mins[栈顶]）是否 < nums[k]
            # 注意：不能用 mins[k-1] 这包含了 最小值可能来自 j 和 k 之间的位置，
            # 而 i 必须在 j 之前，所以只能查 mins[stack[-1]]（范围限定在 j 以内）
            if index_stack and mins[index_stack[-1]] < nums[k]:
                return True

            index_stack.append(k)

        return False


if __name__ == "__main__":
    nums_input_string = "1 2 3 4"
    nums = list(map(int, nums_input_string.split()))
    so = Solution()
    print(so.find_132_pattern(nums))

    nums_input_string_2 = "3 1 4 2"
    nums_2 = list(map(int, nums_input_string_2.split()))
    so_2 = Solution()
    print(so_2.find_132_pattern(nums_2))
