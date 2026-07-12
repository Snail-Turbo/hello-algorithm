def get_b_index(index: int, nums: list[int]) -> int:
    return 0 if nums[index] > nums[-1] else 1  # 核心思路：0 0 0 0 1 1 1        [0》a[n]》1]


class Solution:
    def findMin(self, nums: list[int]) -> int:
        len_nums = len(nums)

        left, right = 0, len_nums - 1

        target = 1

        while left <= right:
            mid_index = (left + right) // 2
            current_value = get_b_index(mid_index, nums)

            if current_value == target:
                right = mid_index - 1
            else:
                left = mid_index + 1

        return nums[left]  # 【关键点】 要的返回值 是 num


input = [3, 4, 5, 1, 2]
