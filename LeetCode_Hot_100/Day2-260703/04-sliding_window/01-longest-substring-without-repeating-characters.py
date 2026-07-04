"""
给定一个字符串s，请你找出其中不含有重复字符的 最长子串 的长度
"""


# 核心思路：如果从 A 到 C 都没有重复，那么从 B 到 C 绝对不可能有重复
# 当我把起点（左手）往右挪一格时，我之前的终点（右手）不需要退回来
# 两个指针同向移动，维护一个连续区间，每次只变一头，另一头不用回头。

class Solution:
    def length_of_longest_substring(self, string:str) -> int:
        
        length_original = len(string)
        char_set = set()

        j = 0
        max_length = 0

        for i in range(length_original):
            while j < length_original and string[j] not in char_set:
                char_set.add(string[j])

                j += 1

            max_length = max(max_length, j-i)

            char_set.remove(string[i])

        return max_length
    
    def length_of_longest_substring_old_school(self, string:str) -> int:
        
        length_original = len(string)
        char_set = set()

        j = -1 # 不同
        max_length = 0

        for i in range(length_original):
            while j < length_original - 1 and string[j+1] not in char_set: # 不同
                char_set.add(string[j])

                j += 1

            max_length = max(max_length, j+1-i) # 不同

            char_set.remove(string[i])

        return max_length