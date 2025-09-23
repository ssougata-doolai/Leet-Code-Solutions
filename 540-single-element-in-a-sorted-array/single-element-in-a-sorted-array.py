class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        n = end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 != 0:
                mid -= 1
            
            if nums[mid] == nums[mid+1]:
                start = mid + 2
            else:
                end = mid
        return nums[start]
            