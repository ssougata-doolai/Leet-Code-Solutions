class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


    # def uniquePaths(self, m: int, n: int) -> int:
    #     memo = {}
    #     res = self.search(m, n, 0, 0, memo)
    #     return res

    # def search(self, m, n, i, j, memo):
    #     if i >= m or j >= n:
    #         return 0   
    #     if i == m-1 and j == n-1:
    #         return 1
    #     if (i, j) in memo:
    #         return memo[(i, j)]
    #     memo[(i, j)] = self.search(m, n, i + 1, j, memo) + self.search(m, n, i, j + 1, memo)
    #     return memo[(i, j)]