

class Solution:
    def find_132_pattern(self, nums: list[int]) -> bool:

        n = len(nums)
        if n < 3:
            return False

        mins = [0] * n  # 这里只需要开辟即可，因为 mins[i] = min(mins[i-1], nums[i])
        mins[0] = nums[0]

        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])

        # 这里使用单调栈，栈中存储的是 nums 的索引，栈是单调递减的
        index_stack = []
        for k in range(n):
            while index_stack and nums[index_stack[-1]] <= nums[k]:
                index_stack.pop()
                # 此时 stack 中剩下的是 nums[k] 左边 的比 nums[k] 大的元素的索引，且stack是单调递减的

            # 10，7，5
            # 若还有元素在栈中，说明 nums[k] 左边还有比 nums[k] 大的元素，且这些元素的索引都在 k 的左边
            # index_stack[-1] 这里不能是 index_stack[-1]-1
            # 因为 当 index_stack[-1] == 0 时，mins[-1] 在 Python 中是合法语法，但取到的是 数组最后一个元素，完全语义错误
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
