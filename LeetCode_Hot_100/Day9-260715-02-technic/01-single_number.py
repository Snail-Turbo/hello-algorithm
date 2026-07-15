from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(Solution().singleNumber(nums))


if __name__ == "__main__":
    main()
