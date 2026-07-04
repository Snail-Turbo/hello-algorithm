"""
给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序输出结果列表。

字母异位词是由重新排列源单词的所有字母得到的一个新单词。
"""

def group_anagrams(strs):
    set_key_dict = {}
    
    for s in strs:
        key = ''.join(sorted(s)) # 核心思路：将每个字符串排序后作为字典的键，所有排序后相同的字符串就是异位词
        set_key_dict.setdefault(key, []).append(s)
    
    return list(set_key_dict.values())


def group_anagrams_upgrade(strs):
    mp = {}

    for s in strs:

        # 核心思路：使用字符计数作为字典的键，所有字符计数相同的字符串就是异位词
        counts = [0] * 26
        for ch in s:
            # 关键点：ord() 函数返回字符的 Unicode 码点，ord('a') 返回 97，ord('b') 返回 98，以此类推。
            counts[ord(ch) - ord('a')] += 1
        
        mp.setdefault(tuple(counts), []).append(s)

    return list(mp.values())


if __name__ == "__main__":

    nums = int(input())
    strs = input().split()

    result = group_anagrams_upgrade(strs)
    result.sort(key=lambda x: (len(x), x))

    for group in result:
        print(' '.join(group))

