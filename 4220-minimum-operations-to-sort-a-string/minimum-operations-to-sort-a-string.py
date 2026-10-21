class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 2 and s[0] > s[1]:
            return -1
        ans = sorted(list(s))
        if list(s) == ans:
            return 0
        s2 = [s[0]] + sorted(list(s)[1:])
        if ans == s2:
            return 1
        s1 = sorted(list(s)[:-1]) + [s[-1]]
        if ans == s1:
            return 1
        if ans == [s1[0]] + sorted(s1[1:]):
            return 2
        if ans == sorted(s2[:-1]) + [s2[-1]]:
            return 2
        return 3