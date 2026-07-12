def _get_type(value, segmant) -> int:
    return 0 if value > segmant else 1

# 关键思路：
# 1. 以 nums[-1] 为分割点 — 旋转数组被分为两段：
#    左段（旋转过来的较大值）> nums[-1]（type 0），
#    右段（有序的较小值）≤ nums[-1]（type 1）。
#
# 2. 同一段内正常二分 — target 和 mid 属于同一类型时，
#    说明在同一个有序区间内，按常规二分比较大小移动指针。
#
# 3. 不同类型时利用段间大小关系：
#    - target < mid（target 在右段，mid 在左段）→ left = mid + 1（向右搜索）
#    - target > mid（target 在左段，mid 在右段）→ right = mid - 1（向左搜索）


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        current_segmant = nums[-1]
        len_nums = len(nums)

        left = 0
        right = len_nums - 1

        target_type = _get_type(target, current_segmant)

        while left <= right:
            mid_index = (left + right) // 2
            current_value = nums[mid_index]
            current_type = _get_type(current_value, current_segmant)

            if target_type == current_type:
                if current_value < target:
                    left = mid_index + 1
                elif current_value > target:
                    right = mid_index - 1
                else:
                    return mid_index
            else:
                if target < current_value:
                    left = mid_index + 1
                else:
                    right = mid_index - 1

        return -1
