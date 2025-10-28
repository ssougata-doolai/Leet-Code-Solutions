class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        res2 = []
        def find_comb(indx, target):
            if indx == n:
                if target == 0:
                    res.append(res2[:])
                return
            
            if candidates[indx] <= target:
                res2.append(candidates[indx])
                find_comb(indx, target-candidates[indx])
                res2.pop()
            find_comb(indx+1, target)
        
        find_comb(0, target)

        return res
