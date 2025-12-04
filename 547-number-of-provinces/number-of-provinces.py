class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if n == 0:
            return 0

        from collections import deque
        visited = [False] * n
        count = 0

        def bfs(i):
            queue = deque([i])
            visited[i] = True

            while queue:
                node = queue.popleft()
                for neighbour in range(n):
                    if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True

        for i in range(n):
            if visited[i] == False:
                bfs(i)
                count += 1
        
        return count

        # n = len(isConnected)
        # if n == 0:
        #     return 0
        # visited = [False] * n
        # count = 0
        # def bfs(i):
        #     queue = deque([i])
        #     visited[i] = True

        #     while queue:
        #         node = queue.popleft()
        #         for j in range(n):
        #             if isConnected[node][j] == 1 and not visited[j]:
        #                 visited[j] = True
        #                 queue.append(j)

        # for i in range(n):
        #     if visited[i] == False:
        #         bfs(i)
        #         count += 1
        
        # return count