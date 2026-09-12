class Solution:
    def firstUniqChar(self, s: str) -> int:
        return next((i for i, c in enumerate(s) if s.count(c) == 1), -1)