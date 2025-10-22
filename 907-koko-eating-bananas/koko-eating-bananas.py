import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_time = max(piles)
        min_time = 1
        l = len(piles)
        
        while min_time <= max_time:
            total_time = 0
            mid = (max_time + min_time) // 2
            for i in range(l):
                total_time += math.ceil(piles[i] / mid)
            
            if total_time <= h:
                max_time = mid - 1
            else:
                min_time = mid + 1

        # print(min_time, max_time)
            
        return min_time

        
        # m = max(piles)
        # for i in range(1, m+1):
        #     total_time = 0
        #     for j in range(len(piles)):
        #         total_time += math.ceil(piles[j] / i)

        #     if total_time <= h:
        #         return i
        
        # return i
