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