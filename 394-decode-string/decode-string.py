class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        number = 0
        current = ""
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == "[":
                stack.append((current, number))
                current = ""
                number = 0
            elif ch == "]":
                previous, repeat = stack.pop()
                current = previous + current * repeat
            else:
                current += ch
        return current