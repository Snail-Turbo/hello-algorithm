"""
给你两个字符串 s 和 t 。请你在 s 中找出包含 t 所有字符的最小子串。如果不存在这样的子串，返回空字符串。
"""
class Solution:
    def min_window(self, original_string:str, target_string:str) -> str:
        if not target_string:
            return ""

        impossible_length = len(original_string) + 1

        need_window = {}
        for char in target_string:
            need_window[char] = need_window.get(char, 0) + 1

        valid = 0 # 重要思路：valid 表示当前窗口中满足 need_window 条件的字符种类数，用于避免每次都去遍历 need_window 来判断当前窗口是否满足条件
        target_valid = len(need_window)

        i = 0
        answer_start = 0
        current_window = {}
        min_length = impossible_length

        for j, char in enumerate(original_string):
            if char in need_window:
                current_window[char] = current_window.get(char, 0) + 1
            
                if current_window[char] == need_window[char]:
                    valid += 1
            
            # 易错：思路是 如果右边满足了，就开始缩小左边才对
            while valid == target_valid: # 这里最极限 i 和 j 相等时，j-i+1=1，表示当前窗口只有一个字符，如果

                current_length = j-i+1
                if current_length < min_length:
                    min_length = current_length
                    answer_start = i

                left_char = original_string[i] 
                if left_char in need_window:
                    current_window[left_char] -= 1

                    if current_window[left_char] < need_window[left_char]:
                        valid -= 1

                i += 1

        return "" if min_length == impossible_length else original_string[answer_start:answer_start+min_length]