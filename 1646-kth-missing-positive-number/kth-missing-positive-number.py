class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

        # def binary_search(arr, k):
        #     min_n = 0
        #     max_n = len(arr) - 1
        #     while min_n <= max_n:
        #         mid = (min_n + max_n) // 2
        #         if arr[mid] == k:
        #             return True
        #         elif k < arr[mid]:
        #             max_n = mid - 1
        #         else:
        #             min_n = mid + 1

        #     return False 

        # def linear_search(arr, k):
        #     for i in range(len(arr)):
        #         if arr[i] == k:
        #             return True
                
        #     return False
        
        # num = 0
        # count = 0
        # while count < k:
        #     num += 1
        #     if binary_search(arr, num) == False:
        #         count += 1
            
        # return num