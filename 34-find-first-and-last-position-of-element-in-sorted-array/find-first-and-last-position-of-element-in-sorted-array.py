class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        l = [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                l[0] = mid
                l[1] = mid

                start1 = start
                end1 = mid - 1
                while start1 <= end1:
                    mid1 = (start1 + end1) // 2
                    if nums[mid1] == target:
                        l[0] = mid1
                        end1 = mid1 - 1
                    elif nums[mid1] > target:
                        end1 = mid1 - 1
                    else:
                        start1 = mid1 + 1

                start2 = mid + 1
                end2 = end
                while start2 <= end2:
                    mid2 = (start2 + end2) // 2
                    if nums[mid2] == target:
                        l[1] = mid2
                        start2 = mid2 + 1
                    elif nums[mid2] > target:
                        end2 = mid2 - 1
                    else:
                        start2 = mid2 + 1
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return l