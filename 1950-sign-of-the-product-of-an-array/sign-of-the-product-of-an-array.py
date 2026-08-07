class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negatives += 1

        if negatives % 2 == 0:
            return 1
        return -1    