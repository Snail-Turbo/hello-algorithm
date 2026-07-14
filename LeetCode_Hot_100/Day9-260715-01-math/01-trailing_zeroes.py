class Solution:
    def trailingZeroes(self, n: int) -> int:

        count_5 = 0

        for num in range(n, 0, -1):

            while num % 5 == 0:
                num //= 5
                count_5 += 1

        return count_5

    def trailingZeroes_per_line(self, n: int) -> int:
        count_5 = 0
        i = 5

        while i <= n:
            count_5 += n // i
            i *= 5

        return count_5


tmp0 = 3
tmp1 = 5
tmp2 = 0


so = Solution()

print(so.trailingZeroes(tmp0))
print(so.trailingZeroes(tmp1))
print(so.trailingZeroes(tmp2))
