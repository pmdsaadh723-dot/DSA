class Solution:  
  def __init__(self):
    self.mod = 10**9 + 7
  def _matmul(self, A, B):
    n = len(A)
    mod = self.mod
    res = [[0] * n for _ in range(n)]
    for i in range(n):
      Ai = A[i]
      for k in range(n):
        Aik = Ai[k]
        if Aik:
          Bk = B[k]
          for j in range(n):
            res[i][j] = (res[i][j] + Aik * Bk[j]) % mod
    return res
  def _matrix_exp(self, M, power):
    n = len(M)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
      res[i][i] = 1
    base = M
    while power > 0:
      if power & 1:
        res = self._matmul(res, base)
      base = self._matmul(base, base)
      power >>= 1
    return res
  def zigZagArrays(self, n, l, r):
    d = r - l + 1
    mod = self.mod
    if n == 1:
      return d % mod
    if n == 2:
      return (d * (d - 1)) % mod
    M = [[0] * d for _ in range(d)]
    for y in range(d):
      cutoff = d - 1 - y
      for j in range(cutoff + 1, d):
        M[y][j] = 1
    v2 = [i for i in range(d)]
    M_exp = self._matrix_exp(M, n - 2)
    final_vec = [0] * d
    for i in range(d):
      row = M_exp[i]
      s = 0
      for j in range(d):
        s += row[j] * v2[j]
      final_vec[i] = s % mod
    return (2 * sum(final_vec)) % mod