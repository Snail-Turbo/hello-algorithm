def compress(s):
    chars = []
    lens = []
    for ch in s:
        if chars and chars[-1] == ch:
            lens[-1] += 1
        else:
            chars.append(ch)
            lens.append(1)
    return chars, lens


def count_good_substrings(a, s):
    ca, la = compress(a)  # 形如：['a', 'b', 'c'], [2, 1, 3]，表示 a = "aabccc"
    cs, ls = compress(s)  # 形如：['a', 'b', 'c'], [2, 1, 3]，表示 s = "aabccc"

    k = len(ca)
    t = len(cs)
    ans = 0

    # A 只有 一种字符
    if k == 1:
        need = la[0]  # 需要 A 中字符的个数
        target_char = la[0]

        for i in range(t):
            if cs[i] == target_char and ls[i] >= need:
                x = ls[i] - need + 1
                ans += x * (x + 1) // 2
        return ans

    # 枚举 S 中连续 k 段
    for i in range(t - k + 1):
        ok = True

        # 检查字符序列和中间段长度
        for j in range(k):
            if cs[i + j] != ca[j]:
                ok = False
                break
            if 0 < j < k - 1 and ls[i + j] < la[j]:
                ok = False
                break

        # 相邻相同字符两个里面可以删一个：所以不能 aaa ggg aaa 把 g 删完

        if not ok:
            continue

        # 检查首尾段长度，并计算可选起点和终点数量
        left_index = i
        right_index = i + k - 1

        # 计算左边段可选起点数量
        left = ls[left_index] - la[0] + 1

        # 计算右边段可选终点数量
        right = ls[right_index] - la[k - 1] + 1

        if left > 0 and right > 0:
            ans += left * right  # 起点在 left 段，终点在 right 段

    return ans


def main():
    n, m = map(int, input().split())
    a = input().strip()
    s = input().strip()

    print(count_good_substrings(a, s))


if __name__ == "__main__":
    main()
