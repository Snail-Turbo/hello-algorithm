"""
给定一个未排序的整数数组nums，要求找出其中没有出现的最小的正整数，并且实现时间复杂度为O(n)且只使用常数级别额外空间的解决方案。

3
1 2 0
"""

# 关键思路：
# 1. 使用集合存储所有正整数，然后从1开始检查每个正整数是否在集合中
# 2. 原地交换：将数组中的每个元素放到其应该在的位置上，最后再遍历一遍数组，找到第一个不在正确位置的元素，其索引+1就是缺失的最小正整数


def first_missing_positive(count, nums):
    if count == 0:
        return 1

    st = set(nums)

    ans = 1
    while ans in st:
        ans += 1

    return ans


def first_missing_positive_inplace(count, nums):
    # 关键思路：将数组中的每个元素放到其应该在的位置上，原地交换，最后再遍历一遍数组，找到第一个不在正确位置的元素，其索引+1就是缺失的最小正整数。
    if count == 0:
        return 1  # 缺少 1 的情况

    for i in range(count):
        # 【关键思路2】：
        # while是为了：被交换过来的元素也要检查是否需要回到正确位置；
        # and 后面的条件是为了防止 2个相同的元素在数组中，导致无限来回交换
        while 1 <= nums[i] <= count and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(count):
        if nums[i] != i + 1:
            return i + 1  # 因为数组索引从0开始，所以要加1

    # 缺少 count+1 的情况 【】
    return count + 1


if __name__ == "__main__":

    """
    3
    1 2 0
    """

    count = int(input())
    nums = list(map(int, input().split()))

    # result = first_missing_positive(count, nums)
    # print(result)

    result_inplace = first_missing_positive_inplace(count, nums)
    print(result_inplace)
