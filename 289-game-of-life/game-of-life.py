class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        board_copy = copy.deepcopy(board)
        def gt(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            else:
                return board[i][j]
        def update(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return
            s = 0
            s += gt(i,j-1)
            s += gt(i-1,j-1)
            s += gt(i-1,j)
            s += gt(i-1,j+1)
            s += gt(i,j+1)
            s += gt(i+1,j+1)
            s += gt(i+1,j)
            s += gt(i+1,j-1)
            if board[i][j]:
                if s<2: board_copy[i][j] = 0
                elif s>3: board_copy[i][j] = 0
            else:
                if s==3: board_copy[i][j] = 1
        for i in range(m):
            for j in range(n):
                update(i,j)
        for i in range(m):
            for j in range(n):
                board[i][j] = board_copy[i][j]