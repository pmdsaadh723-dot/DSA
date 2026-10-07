class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res