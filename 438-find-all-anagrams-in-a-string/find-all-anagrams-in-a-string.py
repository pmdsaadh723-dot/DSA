class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = []
        k = len(p)
        p_count = Counter(p)
        window = Counter()
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if right - left + 1 > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == p_count:
                res.append(left)
        return res