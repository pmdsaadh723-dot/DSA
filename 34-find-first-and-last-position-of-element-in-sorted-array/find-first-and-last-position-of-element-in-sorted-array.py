class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        f, l, r = -1, 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                f =m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        l, r, lt = 0, len(nums) - 1, -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                lt = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [f, lt]
# nums = [5,7,7,8,8,10], target = 8 -------->[3,4]
# nums = [5,7,7,8,8,10], target = 6  -------->[-1,-1]
# nums = [], target = 0 ---------->[-1,-1]