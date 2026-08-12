class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        count = Counter()
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length