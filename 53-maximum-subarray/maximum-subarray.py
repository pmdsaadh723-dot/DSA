class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=nums[0]
        sum=0
        for num in nums:
            if sum<0:
                sum=0
            sum+=num
            maximum=max(maximum,sum)
        return maximum