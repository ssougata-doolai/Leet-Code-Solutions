class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        j = 0

        for i in range(1, n):
            while curr_sum < 1 and j < i:
                curr_sum -= nums[j]
                j += 1
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            
        return max_sum
                