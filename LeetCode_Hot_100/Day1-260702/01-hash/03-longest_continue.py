"""
给定一个未排序的整数数组nums，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为O(n)的算法解决此问题。
"""

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)

    longest_streak = 0

    for num in num_set:
        if num - 1 in num_set:
            continue
        
        current_num = num
        current_streak = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
        
        longest_streak = max(longest_streak, current_streak)

    return longest_streak
    


if __name__ == "__main__":
    num_count = int(input())
    nums = list(map(int, input().split()))
    
    result = longest_consecutive_sequence(nums)
    print(result)