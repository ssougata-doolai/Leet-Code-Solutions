class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l = []
        i, j = 0, -1
        count = m * n
        while m > 0 and n > 0:
            if count < 1:
                break
            for k in range(n):
                j += 1
                l.append(matrix[i][j])
                count -= 1
            m -= 1

            if count < 1:
                break
            for k in range(m):
                i += 1
                l.append(matrix[i][j])
                count -= 1
            n -= 1

            if count < 1:
                break
            for k in range(n):
                j -= 1
                l.append(matrix[i][j])
                count -= 1
            m -= 1

            if count < 1:
                break
            for k in range(m):
                i -= 1
                l.append(matrix[i][j])
                count -= 1
            n -= 1
                
        return l