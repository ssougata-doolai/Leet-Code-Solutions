class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums) // 3
        s = set()
        for i in nums:
            c = d.get(i, 0)
            c += 1
            if c > n:
                s.add(i)
            d[i] = c
        
        return list(s)