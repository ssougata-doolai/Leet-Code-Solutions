class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        l = []
        r, c = len(board), len(board[0])
        queue = deque()

        for i in range(r):
            for j in range(c):
                if (i == 0 or j == 0 or i == r-1 or j == c-1) and board[i][j] == "O":
                    queue.append((i, j))
                    l.append((i, j))
        
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                nr, nc = i+x, j+y
                if 0 <= nr < r and 0 <= nc < c and board[nr][nc] == "O" and (nr, nc) not in l:
                    queue.append((nr, nc))
                    l.append((nr, nc))

        for i in range(r):
            for j in range(c):
                if (i, j) not in l and board[i][j] == "O":
                    board[i][j] = "X"


