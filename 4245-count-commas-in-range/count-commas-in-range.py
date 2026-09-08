class Solution:
    def countCommas(self, n: int) -> int:
        result = 0
        for a in range(1, n + 1):
            if a > 999:
                result += 1
        return result