class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        position = {}

        for i, num in enumerate(sorted_nums):
            if num not in position:
                position[num] = i
            
            result = []
        
        for num in nums:
            result.append(position[num])
        
        return result