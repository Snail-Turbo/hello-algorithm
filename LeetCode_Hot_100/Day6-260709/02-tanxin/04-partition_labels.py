class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 贪心 + 双指针

        last = {}
        len_s = len(s)

        i = 0
        for i in range(len_s):  # 先记住每个字符最晚出现是哪个 index
            last[s[i]] = i

        answer = []
        left = 0  # 用于 计算长度
        right = 0

        for i in range(len_s):  # 从左向右每个字符遍历
            current_char = s[i]

            right = max(right, last[current_char])  # 当前这一段最右侧更新

            if i == right:  # 如果当前这一段字符 最晚出现 没有晚于 right
                answer.append(right-left+1)  # 则当前这一段结束了，记录当前这一段长度 right-left+1
                left = right + 1  # 下一段的left = right+1

        return answer
