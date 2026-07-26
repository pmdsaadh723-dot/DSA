class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * (n + 1)

        for num in nums:
            seen[num] = True
        
        missing = []

        for num in range(1, n + 1):
            if not seen[num]:
                missing.append(num)

        return missing