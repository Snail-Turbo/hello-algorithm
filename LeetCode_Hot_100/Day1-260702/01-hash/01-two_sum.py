"""
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target 的两个整数，并输出它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序输出答案。
"""

def two_sum(num_count, nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in num_to_index:
            return [num_to_index[diff], i]
        
        num_to_index[num] = i
    
    return []

if __name__ == "__main__":
    num_count, target = map(int, input().split())
    nums = list(map(int, input().split()))
    
    result = two_sum(num_count, nums, target)
    print(result)