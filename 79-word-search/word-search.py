class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(row: int, col: int, visited: list, index: int) -> bool:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if visited[row][col]:
                return False
            if board[row][col] == word[index]:
                index += 1
            else:
                return False
            if index == len(word):
                return True
            visited[row][col] = True
            up = dfs(row - 1, col, visited, index)
            down = dfs(row + 1, col, visited, index)
            left = dfs(row, col - 1, visited, index)
            right = dfs(row, col + 1, visited, index)
            visited[row][col] = False
            return up or down or left or right
        for row in range(rows):
            for col in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                if board[row][col] == word[0]:
                    if dfs(row, col, visited, 0):
                        return True
        return False