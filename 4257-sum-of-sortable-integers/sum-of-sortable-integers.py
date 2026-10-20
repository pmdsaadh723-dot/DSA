class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        tl = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            pm = 0
            for base in range(0, n, k):
                desc = 0
                mn, mx = nums[base], nums[base]
                for j in range(k):
                    a = nums[base + j]
                    b = nums[base + (j + 1) % k]
                    if a > b:
                        desc += 1
                    if a < mn: mn = a
                    if a > mx: mx = a
                if desc > 1 or pm > mn:
                    ok = False
                    break
                pm = mx
            if ok:
                tl += k
        return tl