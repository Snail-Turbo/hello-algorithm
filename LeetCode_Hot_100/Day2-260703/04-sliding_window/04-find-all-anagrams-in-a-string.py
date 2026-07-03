"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if n < m:
            return []
        
        target = [0] * 26
        window = [0] * 26

        for char in p:
            target[ord(char) - ord('a')] += 1

        for i, char in enumerate(s[:m]):
            window[ord(char) - ord('a')] += 1

        answers_start_idxs = []

        if window == target:
            answers_start_idxs.append(0) # i-m+1
        
        for j in range(m, n):
            window[ord(s[j]) - ord('a')] += 1
            window[ord(s[j-m]) - ord('a')] -= 1

            if window == target:
                answers_start_idxs.append(j-m+1)
        
        return answers_start_idxs


so = Solution()
s = "abab"
p = "ab"

print(so.findAnagrams(s, p))
        
                
