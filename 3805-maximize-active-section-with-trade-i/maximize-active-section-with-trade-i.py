class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total = 0
        best = 0
        previous_zero = float("-inf")
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            length = j - i
            if s[i] == "1":
                total += length
            else:
                best = max(best, previous_zero + length)
                previous_zero = length
            i = j
        return total + best