class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        indx = -1
        while(start <= end):
            mid = (start + end) // 2
            if nums[mid] == target:
                indx = mid
                return indx
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return indx
            