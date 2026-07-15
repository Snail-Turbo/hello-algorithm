

class Solution:
    def find_132_pattern(self, nums: list[int]) -> bool:

        n = len(nums)
        if n < 3:
            return False

        mins = [float('inf')] * n
        mins[0] = nums[0]

        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])

        stack = []

        for k in range(n):
            while stack and nums[stack[-1]] <= nums[k]:
                stack.pop()
                # 此时 stack 中剩下的是 nums[k] 左边 的比 nums[k] 大的元素的索引，且stack是单调递减的

            if stack and mins[stack[-1]] < nums[k]:
                return True

            stack.append(k)

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
