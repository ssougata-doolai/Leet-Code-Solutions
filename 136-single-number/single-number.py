class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if i != j  and nums[i] == nums[j]:
        #             count += 1
        #     if count == 0:
        #         num = nums[i]
        #         break
        # return num
        
        # Approach 2
        # d = {val: 0 for val in nums}    # Creating dictionary
        # for val in nums:
        #     d[val] += 1
        # for key, value in d.items():    # find from dictionary
        #     if value == 1:
        #         return key

        # Optimal approach
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        
        return res