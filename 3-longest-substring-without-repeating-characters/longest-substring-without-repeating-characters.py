class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len=1
        start=0
        char_index={}
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]]>=start:
                start=char_index[s[end]]+1
            char_index[s[end]]=end
            max_len=max(max_len,end-start+1)
        return max_len