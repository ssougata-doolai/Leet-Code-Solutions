class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        indx = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                indx = mid
                break
            if nums[start] <= nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return indx
