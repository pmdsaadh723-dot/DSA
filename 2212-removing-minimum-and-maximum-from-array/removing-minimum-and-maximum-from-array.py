class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        l, r, n = min(min_index, max_index), max(min_index, max_index), len(nums)
        return min(r + 1, n - l, l + 1 + n - r)