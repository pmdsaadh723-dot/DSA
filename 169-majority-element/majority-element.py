class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = None
        count = 0
        for num in nums:
            if count == 0:
                c = num
            if num == c:
                count += 1
            else:
                count -= 1
        return c