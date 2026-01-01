class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1

                if target < 0:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1

                if target > 0:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
        return result
