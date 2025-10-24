class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = len(weights)
        min_d = max(weights)
        max_d = sum(weights)

        while min_d <= max_d:
            mid = (min_d + max_d) // 2
            count_d = 1
            sum_w = 0
            for i in range(l):
                if sum_w + weights[i] <= mid:
                    sum_w += weights[i]
                else:
                    count_d += 1
                    sum_w = weights[i]
            
            if count_d > days:
                min_d = mid + 1
            else:
                max_d = mid - 1
        
        return min_d

        # Brute force approach
        # while True:
        #     count_d = 0
        #     sum_w = 0
        #     for j in range(l):
        #         if sum_w + weights[j] <= i:
        #             sum_w += weights[j]
        #         else:
        #             count_d += 1
        #             sum_w = weights[j]
        #     count_d += 1
        #     if count_d <= days:
        #         return i
        #     i += 1