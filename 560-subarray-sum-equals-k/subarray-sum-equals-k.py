class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in d:
                count += d[curr_sum - k]
            
            d[curr_sum] = d.get(curr_sum, 0) + 1


        return count