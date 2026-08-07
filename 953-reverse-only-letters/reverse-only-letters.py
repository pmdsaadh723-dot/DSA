class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
        result = []
        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(ch)
        return "".join(result)
        