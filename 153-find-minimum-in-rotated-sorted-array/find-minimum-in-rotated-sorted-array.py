class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        min_v = nums[mid]

        while start < end:
            if nums[start] > nums[mid] and nums[end] > nums[mid]:
                if nums[start] < nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[start] < nums[end]:
                    end = mid - 1
                if nums[start] > nums[end]:
                    start = mid + 1
            
            mid = (start + end) // 2
            if nums[mid] < min_v:
                min_v = nums[mid]
        
        return min_v