import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = len(nums)
        min_n = 1
        max_n = max(nums)

        while min_n <= max_n:
            mid = (min_n + max_n) // 2
            sum_n = 0
            for i in range(l):
                sum_n += math.ceil(nums[i] / mid)
            
            if sum_n <= threshold:
                max_n = mid - 1
            else:
                min_n = mid + 1
            
        return min_n
        
        # Brute force approach
        # for i in range(1, max_n+1):
        #     sum_n = 0
        #     for j in range(l):
        #         sum_n += math.ceil(nums[j] / i)

        #     if sum_n <= threshold:
        #         return i