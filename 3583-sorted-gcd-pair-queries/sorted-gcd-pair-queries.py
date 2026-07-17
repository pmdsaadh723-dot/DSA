class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        gcdCnt = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            cnt = 0
            for x in range(g, mx + 1, g):
                cnt += freq[x]
            gcdCnt[g] = cnt * (cnt - 1) // 2
            for x in range(g * 2, mx + 1, g):
                gcdCnt[g] -= gcdCnt[x]
        prefix = list(accumulate(gcdCnt))
        return [bisect_right(prefix, q) for q in queries]