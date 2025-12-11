class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        r, c = len(mat), len(mat[0])
        mat2 = [[float('inf')]*c for _ in range(r)]

        queue = deque()
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    mat2[i][j] = 0
                    queue.append((i, j))
        
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                nr, nc = i + x, j + y
                if 0 <= nr < r and 0 <= nc < c:
                    if mat2[nr][nc] > mat2[i][j] + 1:
                        mat2[nr][nc] = mat2[i][j] + 1
                        queue.append((nr, nc))

        return mat2