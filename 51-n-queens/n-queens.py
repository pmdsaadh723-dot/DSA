class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        return [
            ["." * i + "Q" + "." * (n - i - 1) for i in p]
            for p in permutations(range(n))
            if len(set(i - j for i, j in enumerate(p))) == 
               len(set(i + j for i, j in enumerate(p))) == n
]