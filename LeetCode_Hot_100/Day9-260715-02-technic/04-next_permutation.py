from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        len_nums = len(nums)

        for i in range(len_nums - 2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return nums

        target_index = i
        target_num = nums[i]

        for j in range(len_nums-1, target_index, -1):
            if nums[j] > target_num:
                nums[j], nums[target_index] = nums[target_index], nums[j]
                break

        # [target_index+1 : ] 进行反转
        left, right = target_index + 1, len_nums - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# 这种情况 不能在从右向左找第一个大于他的时候 顺便反转：
# 2.5, 4, 3, 2.6, 1, 0
# 0, 3, 2.6, 1, 4
# 0, 1, 2.6, 3, 4


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    Solution().nextPermutation(nums)
    print(" ".join(map(str, nums)))


if __name__ == "__main__":
    main()
