class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        res2 = []
        n = len(candidates)
        candidates.sort()

        def find_comb(indx, target):
            if target == 0:
                res.append(res2[:])
                return
            
            for i in range(indx, n):
                if i > indx and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                res2.append(candidates[i])
                find_comb(i+1, target-candidates[i])
                res2.pop()

        find_comb(0, target)
        return res