import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if_need_average = (len_nums1 + len_nums2) % 2 == 0

        i = 0
        j = 0

        tmp_list = []

        while i < len_nums1 and j < len_nums2:
            if nums1[i] < nums2[j]:
                tmp_list.append(nums1[i])
                i += 1
            else:
                tmp_list.append(nums2[j])
                j += 1

        while i < len_nums1:
            tmp_list.append(nums1[i])
            i += 1

        while j < len_nums2:
            tmp_list.append(nums2[j])
            j += 1

        n = len(tmp_list)

        if if_need_average:
            return (tmp_list[n//2-1] + tmp_list[n//2]) / 2

        return tmp_list[n//2]

    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        totoal_length = len_nums1 + len_nums2
        if_need_average = totoal_length % 2 == 0

        target_count = (totoal_length - 1) // 2

        i, j = 0, 0

        def get_next():
            nonlocal i, j

            if i >= len_nums1:
                j += 1
                return nums2[j-1]

            if j >= len_nums2:
                i += 1
                return nums1[i-1]

            if nums1[i] < nums2[j]:
                i += 1
                return nums1[i-1]

            j += 1
            return nums2[j-1]

        for _ in range(target_count):
            get_next()

        if if_need_average:
            val1 = get_next()
            val2 = get_next()
            return (val1 + val2) / 2

        return get_next()

    def findMedianSortedArrays_cut_list(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        len_nums1 = len(A)
        len_nums2 = len(B)
        totla_length = len_nums1 + len_nums2

        half_count = (totla_length + 1) // 2

        for i in range(totla_length + 1):
            j = half_count - i

            if j < 0 or j > len_nums2:
                continue

            A_left = A[i-1] if i > 0 else float("-inf")
            A_right = A[i] if i < len_nums1 else float("inf")

            B_left = B[j-1] if j > 0 else float("-inf")
            B_right = B[j] if j < len_nums2 else float("inf")

            max_pre = max(A_left, B_left)
            min_suf = min(A_right, B_right)

            if max_pre <= min_suf:
                if totla_length % 2 == 1:
                    return max_pre

                return (max_pre + min_suf) / 2

        return 0.0

    def findMedianSortedArrays_cut_list_binary(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        n, m = len(A), len(B)

        total = n+m
        half_count = (total + 1) // 2

        left, right = 0, n

        while left <= right:
            i = (left + right) // 2

            j = half_count - i

            A_left = A[i-1] if i > 0 else float("-inf")
            A_right = A[i] if i < n else float("inf")
            B_left = B[j-1] if j > 0 else float("-inf")
            B_right = B[j] if j < m else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return max(A_left, B_left)

                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            elif A_left > B_right:
                right = i-1
            else:
                left = i + 1

        return 0.0


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    idx = 0
    m = int(data[idx])
    idx += 1

    nums1 = []
    for _ in range(m):
        nums1.append(int(data[idx]))
        idx += 1

    n = int(data[idx])
    idx += 1

    nums2 = []
    for _ in range(n):
        nums2.append(int(data[idx]))
        idx += 1

    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"{ans:.5f}")


if __name__ == "__main__":
    main()
