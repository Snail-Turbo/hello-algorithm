
class Solution:
    def min_window(self, original_string:str, target_string:str) -> str:
        impossible_big_count = len(original_string) + 1

        need = {}

        for char in target_string:
            need[char] = need.get(char, 0) + 1

        valid = 0
        target_valid = len(need)

        window = {}

        i = 0
        start = 0
        min_len = impossible_big_count

        for j, char in enumerate(original_string):
            if char in need:
                window[char] = window.get(char, 0) + 1

                if window[char] == need[char]:
                    valid += 1

            
            while valid == target_valid:
                if j-i+1 < min_len:
                    min_len = j-i+1
                    start = i

                left_char = original_string[i]

                if left_char in need:
                    if window[left_char] == need[left_char]:
                        valid -= 1
                    window[left_char] -= 1
                
                i += 1

        return "" if min_len == impossible_big_count else original_string[start:start+min_len]