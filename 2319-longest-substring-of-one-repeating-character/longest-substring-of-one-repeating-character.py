class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)
        left = [""] * (4 * n)
        right = [""] * (4 * n)
        def build(i, l, r):
            if l == r:
                pre[i] = suf[i] = best[i] = 1
                left[i] = right[i] = s[l]
                return
            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            merge(i, l, r)
        def merge(i, l, r):
            m = (l + r) // 2
            a, b = i * 2, i * 2 + 1
            left[i], right[i] = left[a], right[b]
            pre[i] = pre[a]
            suf[i] = suf[b]
            if right[a] == left[b]:
                best[i] = max(best[a], best[b], suf[a] + pre[b])
                if pre[a] == m - l + 1:
                    pre[i] += pre[b]
                if suf[b] == r - m:
                    suf[i] += suf[a]
            else:
                best[i] = max(best[a], best[b])
        def update(i, l, r, pos, ch):
            if l == r:
                left[i] = right[i] = ch
                return
            m = (l + r) // 2
            if pos <= m:
                update(i * 2, l, m, pos, ch)
            else:
                update(i * 2 + 1, m + 1, r, pos, ch)
            merge(i, l, r)
        build(1, 0, n - 1)
        ans = []
        for pos, ch in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, pos, ch)
            ans.append(best[1])
        return ans