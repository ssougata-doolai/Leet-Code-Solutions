class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if color == old_color:
            return image
        
        from collections import deque
        r, c = len(image), len(image[0])
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color

        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                nr = i + x
                nc = j + y
                if 0 <= nr < r and 0 <= nc < c and image[nr][nc] == old_color:
                    queue.append((nr, nc))
                    image[nr][nc] = color

        return image
