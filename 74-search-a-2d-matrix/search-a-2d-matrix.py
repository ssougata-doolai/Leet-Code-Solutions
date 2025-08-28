class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for row in matrix:
            l = len(row)
            if target >= row[0] and target <= row[l-1]:
                beg = 0
                end = l - 1
                while beg <= end:
                    mid = (beg + end) // 2
                    # print(f"beg: {beg}, end: {end}")
                    if row[mid] == target:
                        flag = True
                        break
                    elif target > row[mid]:
                        beg = mid + 1
                    else:
                        end = mid - 1

        return flag
