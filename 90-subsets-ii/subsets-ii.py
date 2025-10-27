class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def find_sub(indx, res2):
            if indx == n:
                res3 = list(res2)
                res3.sort()
                if res3 not in res:
                    res.append(res3)
                return
            find_sub(indx+1, res2)
            res2.append(nums[indx])
            find_sub(indx+1, res2)
            res2.pop()
            
        find_sub(0, [])
        return res