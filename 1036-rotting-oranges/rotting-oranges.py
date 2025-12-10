class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        row, col = len(grid), len(grid[0])

        queue = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = 0
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

        # BFS traversal
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for d1, d2 in directions:
                    nr = r + d1
                    nc = c + d2

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                    
            time += 1
        
        return time-1 if fresh == 0 else -1

