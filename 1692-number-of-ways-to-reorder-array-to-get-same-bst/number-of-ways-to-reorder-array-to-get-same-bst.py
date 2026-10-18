class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        position = [0] * (n + 1)
        for i, value in enumerate(nums):
            position[value] = i
        parent = [0] * (n + 1)
        stack = []
        factorial = 1
        for value in range(1, n + 1):
            factorial = factorial * value % mod
            last = 0
            while stack and position[stack[-1]] > position[value]:
                last = stack.pop()
            if stack:
                parent[value] = stack[-1]
            if last:
                parent[last] = value
            stack.append(value)
        size = [1] * (n + 1)
        denominator = 1
        for value in reversed(nums):
            denominator = denominator * size[value] % mod
            if parent[value]:
                size[parent[value]] += size[value]
        return (factorial * pow(denominator, mod - 2, mod) - 1) % mod